from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=100)
    Body = models.CharField(max_length=100000000)
    created_at =models.DateTimeField(default=datetime.now,blank=True)