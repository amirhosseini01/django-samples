from django.db import models
import uuid

# Create your models here.
class FirstApp(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=2000, null=True, blank=True)
    link = models.CharField(max_length=2000, null=True, blank=True)
    createAt = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)

    def __str__(self):
        return self.title