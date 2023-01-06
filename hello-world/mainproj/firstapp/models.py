from django.db import models
import uuid

# Create your models here.
from users.models import Profile
class FirstApp(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=2000, null=True, blank=True)
    link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    img = models.ImageField(default= "default.jpg", null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    createAt = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)

    def __str__(self):
        return self.title

class Review(models.Model):
    firstApp = models.ForeignKey(FirstApp, on_delete= models.CASCADE)
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    value  = models.CharField(max_length=200, choices=VOTE_TYPE)
    createAt = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    title = models.CharField(max_length=200)
    createAt = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)
    
    def __str__(self):
        return self.title