from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'dashboard_index'),

    #ajax
    path('ajax-date-filter', views.dateFilter, name='date_filter')
]
