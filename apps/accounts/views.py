from django.contrib import messages, auth
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from apps.accounts.decorators import admin_only

@login_required
@admin_only
def index(request):
  users = User.objects.all()
  return render(request, 'accounts/index.html', {'users': users})

@login_required
@admin_only
def add(request):
  return render(request, 'accounts/add.html')


@login_required
@admin_only
def addSave(request):
    if request.method != 'POST':
        return render(request, 'accounts/add.html')

    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    if not firstname or not lastname or not email or not username or not password or not password2:
        messages.error(request,"You must to fill all fields")
        return render(request, 'accounts/add.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request,'email invalid')
        return render(request, 'accounts/add.html')

    if len(password) < 6:
        messages.error(request, 'Password must be minimum 6 letters.')
        return render(request, 'accounts/add.html')

    if len(username) < 4:
        messages.error(request, 'Username must be minimum 4 letters.')
        return render(request, 'accounts/add.html')

    if password != password2:
        messages.error(request, 'Password not match')
        return render(request, 'accounts/add.html')

    if User.objects.filter(username = username).exists():
        messages.error(request, 'Username already exists, please change.')
        return render(request, 'accounts/add.html')

    if User.objects.filter(email = email).exists():
        messages.error(request, 'Email already exists, please change.')
        return render(request, 'accounts/add.html')

    user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password, 
            first_name = firstname, 
            last_name=lastname)
    user.save()

    return redirect('account_index')

@login_required
@admin_only
def edit(request, id):
  if request.method == 'GET':
    user = User.objects.get(id = id)
    return render(request, 'accounts/edit.html', {'user': user})


@login_required
@admin_only
def editSave(request, id):
  if request.method == "POST":
    company = get_object_or_404(User, id=id)
    return redirect ('account_index')
  else:
    messages.error(request, "Error when edit")
    return edit(request, id)

@login_required
@admin_only
def delete(request):
  if request.method == "GET":
    id = request.GET.get('id', None)
    user = get_object_or_404(User, id=id)
    user.delete()
    data = {
      'delete': 1
      }
  else:
    data = {
      'delete': 0
      }
  return JsonResponse(data)

def Login(request):
  if request.method != 'POST':
        return render(request, 'accounts/login.html')
  username = request.POST.get('username')
  password = request.POST.get('password')
  user = auth.authenticate(request, username=username, password=password)
  if not user:
      messages.error(request, 'Usuário ou senha Invalido')
      return render(request, 'accounts/login.html')
      
  else:
      auth.login(request, user)
      return redirect('dashboard_index')

def Logout(request):
  auth.logout(request)
  return render(request, 'accounts/login.html')