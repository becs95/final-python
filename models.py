from django.db import models
from django import forms

# Create your models here.
class InformacionForm(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField(max_length=100)
    cantidad_videos = forms.IntegerField()


class Video(models.Model):
    titulo = models.CharField(max_length=100)
    nombre_video = models.CharField(max_length=100)
    extension = models.CharField(max_length=10)
    tamano = models.FloatField()