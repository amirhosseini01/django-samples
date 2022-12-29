from django.contrib import admin

# Register your models here.

from .models import FirstApp, Review, Tag
admin.site.register(FirstApp)
admin.site.register(Review)
admin.site.register(Tag)