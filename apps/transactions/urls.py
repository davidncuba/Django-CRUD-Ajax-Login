from django.urls import path
from . import views

urlpatterns = [
    path('depature/', views.depatureIndex, name='depature_index'),
    path('depature-add/', views.depatureAdd, name='depature_add'),
    path('depature-save/', views.depatureAddSave, name='depature_save'),
    path('depature-delete/', views.depatureDelete, name='depature_delete'),
    path('depature-edit/<int:id>/', views.depatureEdit, name='depature_edit'),
    path('depature-edit-save/<int:id>/', views.depatureEditSave, name='depature_edit_save'),
    path('delivered/', views.deliveredIndex, name='delivered_index'),
    path('delivered-add/', views.deliveredIndex, name='delivered_add'),
    path('delivered-delete/', views.deliveredIndex, name='delivered_delete'),


    path('ajax/driver/', views.loadDriverAjax, name='ajax_driver'),
    path('ajax/delivery/driver', views.loadDeliveryDriver, name='ajax_delivery_driver'),
    path('ajax/delivery/confirm', views.deliveryConfirm, name='ajax_delivery_confirm'),

  ]