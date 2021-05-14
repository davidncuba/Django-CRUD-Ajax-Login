from django.db import models

# Create your models here.

class Company(models.Model):
  name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  street = models.CharField(max_length=100)
  number = models.CharField(max_length=30)
  postcode = models.CharField(max_length=50)  

  def __str__(self):
    return self.name
