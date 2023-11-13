#views of bio directory

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("HELLO PG BIO")
