from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'company_index'),
    path('add', views.add, name= 'company_add'),
    path('edit/<int:id>', views.edit, name= 'company_edit'),
    path('edit_save/<int:id>', views.saveEdit, name= 'company_edit_save'),
    path('delete/', views.delete, name= 'company_delete'),
]
