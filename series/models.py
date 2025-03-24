from django.db import models


class Series(models.Model):
    title = models.CharField(max_length=100, help_text='Serial nomi')
    description = models.TextField(help_text='Serial haqida ma\'lumot')
    first_episode = models.CharField(max_length=100, help_text='Serialning birinchi qismi')
    location = models.CharField(max_length=100, help_text='Serial qaysi joyda suratga olingan')
    producer = models.CharField(max_length=100, help_text='Serialni suratga olgan inson')
    music_author = models.CharField(max_length=100, help_text='Serial musiqasi muallifi')
    studio = models.CharField(max_length=100, help_text='Serialni suratga olgan studiya')
    telegram_channel = models.CharField(max_length=100, help_text='Serialning telegram kanali')
    plot = models.TextField(help_text='Serialning mazmuni')
    poster = models.ImageField(upload_to="posters/", help_text='Serialning rasmi')
    backdrop = models.ImageField(upload_to="backdrops/", null=True, blank=True, help_text='Serialning fon rasmi')

    def __str__(self):
        return self.title


class Casts(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, help_text='Qaysi serialga tegishli ekanligi')
    cast = models.CharField(max_length=100, help_text='Serialdagi qahramon')
    description = models.TextField(help_text='Qahramon haqida ma\'lumot')

    def __str__(self):
        return self.cast


class Episode(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, help_text='Episode qaysi serialga tegishli ekanligi')
    title = models.CharField(max_length=10, help_text='Episode nomi (1-qism)')
    part = models.IntegerField(help_text='Qism (raqamlarda)')
    image = models.ImageField(upload_to="episodes/", null=True, blank=True, help_text='Episode rasmi')
    link = models.CharField(max_length=255, help_text='Episode linki')

    def __str__(self):
        return self.series.title
