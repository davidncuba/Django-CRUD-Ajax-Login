from django.db import models
from apps.company.models import Company
from django.contrib.auth.models import User
# Create your models here.
class Transactions(models.Model):
  driver = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  departure = models.ForeignKey(Company, on_delete=models.DO_NOTHING, related_name='received')
  date_depature = models.DateTimeField(auto_now_add=True)
  delivery = models.ForeignKey(Company, on_delete=models.DO_NOTHING,null=True, blank=True)
  date_delivered = models.DateTimeField(null=True, blank=True)
  
  
