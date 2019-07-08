from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_date',)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.text
    
    
    class Meta:
        ordering = ('created_date',)
