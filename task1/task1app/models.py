from django.db import models


# Create your models here.
class team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()


class destinations(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics_dest')
    desc = models.TextField()
