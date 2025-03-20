from django.db import models


# Create your models here.


class Series(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    first_episode = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    music_author = models.CharField(max_length=100)
    studio = models.CharField(max_length=100)
    telegram_channel = models.CharField(max_length=100)
    plot = models.TextField()
    poster = models.ImageField(upload_to="series/posters")
    backdrop = models.ImageField(upload_to="series/backdrops", null=True, blank=True)

    def __str__(self):
        return self.title


class Casts(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    cast = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.cast


class Episode(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    part = models.CharField(max_length=20)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.series.title
