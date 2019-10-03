from django.urls import path
from . import views

urlpatterns = [
    path('', views.urls_list,name='urls_list'),
]