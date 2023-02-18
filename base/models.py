from django.db import models
import uuid                      #what is it - it makes unique id
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    slug = models.SlugField(null =True, blank = True)       #difference between null and blank in postgre 
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def _str_(self):
        return self.title 


class Skill(models.Model) :
    title = models.CharField(max_length=200)
    body  = models.TextField(null =True, blank=True)
    created = models.DateTimeField(auto_now_add=True)   

    def _str_(self):
       return self.title 


class Tag(models.Model) :
    name = models.CharField(max_length=200,null =True)
    created = models.DateTimeField(auto_now_add=True)   

    def _str_(self):
       return self.name

