from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    image = models.ImageField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
     return self.title
