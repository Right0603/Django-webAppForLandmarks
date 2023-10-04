from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
   title = models.CharField(max_length=30)
   description = models.TextField(blank=True, null=True)

   def __str__(self):
      return self.title
   
   class Meta:
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    image = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
     return self.title          
    

