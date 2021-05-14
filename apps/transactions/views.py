from apps.company.models import Company
from .forms import TransactionsFormEdit
from .models import Transactions
from apps.driver.models import Driver
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from datetime import datetime 

@login_required
def depatureIndex(request):
  depatures = Transactions.objects.all().values('id', 'driver__username', 'departure__name', 'delivery__name', 'date_depature')
  return render(request, 'depature/index.html', {'depatures': depatures})

@login_required
def depatureAdd(request):
  companys = Company.objects.all()

  return render(request, 'depature/add.html', {'companys': companys})

@login_required
def depatureEdit(request, id):
  if request.method == 'GET':
    transaction = Transactions.objects.get(id = id)
    form = TransactionsFormEdit(instance=transaction)
  return render(request, 'depature/edit.html', {'transaction': transaction, 'form': form})

@login_required
def depatureAddSave(request):
  if request.POST.get('departure', '')  == "Select" \
    or request.POST.get('delivery', '')  == "Select" \
    or request.POST.get('driver', '') == "Select":
    
    messages.error(request, "You must fill all fields.")
    
    companys = Company.objects.all()

    return render(request, 'depature/add.html', {'companys': companys})

  departure = request.POST.get('departure', '')
  delivery = request.POST.get('delivery', '')
  driver = request.POST.get('driver', '')
  departure = get_object_or_404(Company, id=departure)
  delivery = get_object_or_404(Company, id=delivery)
  driver = get_object_or_404(User, id=driver)

  transactions = Transactions(
    departure = departure,
    delivery = delivery,
    driver = driver
  )
  transactions.save()

  return redirect('depature_index')

@login_required
def depatureDelete(request):
  if request.method == "GET":
    id = request.GET.get('id', None)
    depature = get_object_or_404(Transactions, id=id)
    depature.delete()
    data = {
      'delete': 1
      }
  else:
    data = {
      'delete': 0
      }
  return JsonResponse(data)

@login_required
def depatureEditSave(request, id):
   if request.method == "POST":
    transactions = get_object_or_404(Transactions, pk=id)
    form = TransactionsFormEdit(request.POST, instance=transactions)
    if form.is_valid():
      form.save()
      return redirect ('depature_index')
    else:
      messages.error(request, "Error when edit")
      return depatureEdit(request, id)

@login_required
def deliveredIndex(request):
  companys = Company.objects.all()
  return render(request, 'delivered/index.html',  {'companys': companys})

@login_required
def loadDriverAjax(request):
  id = request.GET.get('id', None)
  drivers = Driver.objects.all().filter(company = id)
  return render(request, 'depature/ajax/driver.html', {'drivers': drivers}) 

@login_required
def loadDeliveryDriver(request):
  id = request.GET.get('id', None)
 
  transactions = Transactions.objects.all().filter(delivery=id).filter(date_delivered__isnull=True)
  return render(request, 'delivered/ajax/deliver.html', {'transactions': transactions}) 

@login_required
def deliveryConfirm(request):
  if request.method == "GET":
    id = request.GET.get('id', None)
    Transactions.objects.filter(id=id).update(date_delivered =datetime.now())
    
    data = {
      'delete': 1
      }
  else:
    data = {
      'delete': 0
      }
  return JsonResponse(data)