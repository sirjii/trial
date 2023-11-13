#urls.py of bio directory

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index1'),
    path('login_user',views.login_user,name='login'),
    path('logout_user',views.logout_user,name='logout'),
    path('register_user',views.register_user,name='register'),
    path('send_email',views.send_email_to_client,name='send_email'),
    path('search_result',views.search_result,name='search')
]