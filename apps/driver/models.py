from django.db import models
from django.contrib.auth.models import User 
from apps.company.models import Company
# Create your models here.

class Driver(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
