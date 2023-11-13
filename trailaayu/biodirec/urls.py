#urls.py of bio directory

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='bioindex'),
]