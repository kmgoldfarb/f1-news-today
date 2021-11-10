from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    image = models.CharField(max_length=1000)
    alt = models.CharField(max_length=500, default="")
    site = models.CharField(max_length=500)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Driver(models.Model):
    position = models.IntegerField()
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=10)
    team = models.CharField(max_length=100)
    points = models.FloatField()

    def __str__(self):
        return self.last_name


class Constructor(models.Model):
    position = models.IntegerField
    team = models.CharField(max_length=100)
    points = models.IntegerField

    def __str__(self):
        return self.team
