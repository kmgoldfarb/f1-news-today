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
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=10)
    team = models.CharField(max_length=100)
    points = models.FloatField()

    def __str__(self):
        return self.name


class Constructor(models.Model):
    position = models.IntegerField()
    team = models.CharField(max_length=100)
    points = models.FloatField()

    def __str__(self):
        return self.team


class Race(models.Model):
    title = models.CharField(max_length=300)
    date = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    flag = models.CharField(max_length=500)
    track_img = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.title