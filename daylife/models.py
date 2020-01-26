from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=32)

class Daylife(models.Model):
    title = models.CharField(max_length=32)
    date = models.CharField(max_length=32)
    detail = models.CharField(max_length=32)
    logo = models.ImageField(upload_to='daylife/images')

class Daystory(models.Model):
    story = models.CharField(max_length=32)
    pic = models.ImageField(upload_to='daylife/images')
    daylife = models.ForeignKey(to='Daylife',on_delete=models.CASCADE)


