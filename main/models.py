from django.db import models
import datetime

class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    image = models.ImageField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
     return self.title
    
class Category(models.Model):
   title = models.CharField(max_length=30)
   description = models.TextField()

