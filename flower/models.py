from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=32)
    introduce = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='flower/images')

class FlowewrPic(models.Model):
    fpicture = models.ImageField(upload_to='flower/images')
    flower = models.ForeignKey(to='Flower',on_delete=models.CASCADE)
