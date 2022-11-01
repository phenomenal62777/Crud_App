from pyexpat import model
from cv2 import integral
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class student (models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=20)