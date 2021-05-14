from .forms import CompanyForm
from .models import Company
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import admin_only
from django.shortcuts import render, redirect, get_object_or_404

@login_required
@admin_only
def index(request):
  if request.method == "POST":
    form = CompanyForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect ('company_index')
    else:
      messages.error(request, "Name Already exists.")
      return add(request)

  companys = Company.objects.all()

  return render(request, 'company/index.html', {'companys': companys})

@login_required
@admin_only
def add(request):
  form = CompanyForm()

  return render(request, 'company/add.html', {'form': form})

@login_required
@admin_only
def edit(request, id):
  if request.method == "GET":
    company = Company.objects.get(id = id)
    form = CompanyForm(instance = company)
    return render(request, 'company/edit.html', {'company': company, 'form': form})

@login_required
@admin_only
def saveEdit(request, id):
  if request.method == "POST":
    company = get_object_or_404(Company, id=id)
    form = CompanyForm(request.POST, instance=company)
    if form.is_valid():
      form.save()
      return redirect ('company_index')
    else:
      messages.error(request, "Error when edit")
      return edit(request, id)
     
@login_required
@admin_only
def delete(request):
  if request.method == "GET":
    id = request.GET.get('id', None)
    company = get_object_or_404(Company, id=id)
    company.delete()
    data = {
      'delete': 1
      }
  else:
    data = {
      'delete': 0
      }
  return JsonResponse(data)

