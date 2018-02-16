
from django.db import models
# Create your models here.



class front(models.Model):
    title = models.CharField(max_length=200)


    image1 = models.ImageField(upload_to='static/img/')
    image2 = models.ImageField(upload_to='static/img/')
    image3 = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.title


class section1(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='static/img/')


    def __str__(self):
        return self.title


class section2(models.Model):
    title = models.CharField(max_length=200)

    text = models.CharField(max_length=200)
    subText = models.CharField(max_length=200)


    image = models.ImageField(upload_to='static/img/')



    def __str__(self):
        return self.title





