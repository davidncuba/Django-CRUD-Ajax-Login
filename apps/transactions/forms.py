from .models import Transactions
from django import forms

class TransactionsFormEdit(forms.ModelForm):
  class Meta:
    model = Transactions
    fields = ('driver',)