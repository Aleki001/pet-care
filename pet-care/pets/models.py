from django.db import models

class Pets(models.Model):
    name = models.CharField(max_length=100)
    gender_age = models.CharField(max_length=300)
    hair_type = models.CharField(max_length=300)
    origin = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='pets/')
