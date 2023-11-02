from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
   title = models.CharField(max_length=60)
   description = models.TextField(blank=True, null=True)

   def __str__(self):
      return self.title
   
   class Meta:
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
     return self.title 

class Image(models.Model):
   image = models.ImageField(upload_to='images/')  
   article = models.ForeignKey(Article, on_delete=models.CASCADE)

       


    

