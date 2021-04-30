from django.db import models


# Create your models here.
class Allbum(models.Model):
    thumbnail = models.ImageField(upload_to='album/photo')
    tittle = models.TextField(max_length=50)
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)