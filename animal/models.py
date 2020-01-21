from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    descript = models.CharField(max_length=64)

class AnimalStore(models.Model):
    title = models.CharField(max_length=32)
    loge = models.ImageField(upload_to='animal/images')
    store = models.TextField()
    origin = models.CharField(max_length=32)
    data = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    animal = models.ForeignKey('Animal',on_delete=models.CASCADE)

class AnimalPic(models.Model):
    apicture = models.ImageField(upload_to='animal/images')
    animal = models.ForeignKey('Animal',on_delete=models.CASCADE)
    animalstore = models.ForeignKey('AnimalStore',on_delete=models.CASCADE)
