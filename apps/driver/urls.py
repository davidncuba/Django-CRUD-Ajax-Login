from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'driver_index'),
    path('add/', views.add, name= 'driver_add'),
    path('add-save/', views.addSave, name= 'driver_save'), 
    path('edit/<int:id>', views.edit, name= 'driver_edit'), 
    path('edit-save/<int:id>', views.editSave, name= 'driver_edit_save'), 
    path('delete/', views.delete, name= 'driver_delete'), 
]
