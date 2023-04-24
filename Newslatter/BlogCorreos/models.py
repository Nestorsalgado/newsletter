from django.db import models
import datetime

class Post (models.Model):
    titulo = models.CharField(max_length=100)
    descripcion= models.TextField()
    image=models.ImageField(upload_to='blog/image')
    date=models.DateField(datetime.date.today)
