from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='account_index'),
    path('add', views.add, name='account_add'),
    path('add_save', views.addSave, name='account_save'),
    path('edit/<int:id>', views.edit, name='account_edit'),
    path('edit_save/<int:id>', views.editSave, name='account_edit_save'),
    path('delete/', views.delete, name= 'account_delete'),

    path('login/', views.Login, name='login'),
    path('login/', views.Logout, name='logout'),

  ]