from .models import Driver
from django import forms

class DriverForm(forms.ModelForm):
  class Meta:
    model = Driver
    fields = '__all__'

class DriverFormEdit(forms.ModelForm):
  class Meta:
    model = Driver
    fields = ('company',)