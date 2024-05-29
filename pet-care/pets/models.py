from django.db import models

class Pets(models.Model):
    name = models.CharField(max_length=100)
    gender_age = models.CharField(max_length=300)
    hair_type = models.CharField(max_length=300)
    origin = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='pets/')

    def __str__(self):
        return self.name



class AdoptionRequest(models.Model):
    pet_name = models.CharField(max_length=100, default="zone") 
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)

    def __str__(self):
        return self.name