from .forms import DriverForm, DriverFormEdit
from .models import Driver
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from apps.accounts.decorators import admin_only

@login_required
@admin_only
def index(request):
  drivers = Driver.objects.all()

  return render(request, 'driver/index.html', {'drivers': drivers })

@login_required
@admin_only
def add(request):
  form = DriverForm()
  return render(request, 'driver/add.html', { 'form': form })

@login_required
@admin_only
def addSave(request):
  if request.method == 'POST':
    form = DriverForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect ('driver_index')
    else:
      messages.error(request, 'Driver in another company please select another')
      return add(request)

@login_required
@admin_only
def edit(request, id):
  if request.method == 'GET':
    driver = Driver.objects.get(id = id)
    form = DriverFormEdit(instance=driver)
    return render(request, 'driver/edit.html', {'driver': driver, 'form': form})

@login_required
@admin_only
def editSave(request, id):
  if request.method == "POST":
    driver = get_object_or_404(Driver, pk=id)
    form = DriverFormEdit(request.POST, instance=driver)
    if form.is_valid():
      form.save()
      return redirect ('driver_index')
    else:
      messages.error(request, "Error when edit")
      return edit(request, id)

@login_required
@admin_only
def delete(request):
  if request.method == "GET":
    id = request.GET.get('id', None)
    driver = get_object_or_404(Driver, id=id)
    driver.delete()
    data = {
      'delete': 1
      }
  else:
    data = {
      'delete': 0
      }
  return JsonResponse(data)