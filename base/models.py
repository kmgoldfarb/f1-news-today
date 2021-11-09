from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    image = models.CharField(max_length=1000)
    alt = models.CharField(max_length=500, default="")
    site = models.CharField(max_length=500)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.title
        