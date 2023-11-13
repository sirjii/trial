#views of scan upload app

from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

from .utils import send_email_to_client


# Create your views here.


def index(request):
    return HttpResponse("bye")
    #return render(request,'index.html')
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        usercheck=User.objects.filter(username=username)
        if not usercheck.exists():
            messages.success(request,("username not found "))
            return redirect('login')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('/?example_param=' + username)
            else:
                messages.success(request,("kindly enter the right password"))
                return redirect('login')
                # Return an 'invalid login' error message.
    else:
        return render(request,'login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,("logout successfully"))
    return redirect('Home')

def register_user(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password=request.POST.get('password')

        #checking for already taken usename
        user=User.objects.filter(username=username)

        if user.exists():
            messages.success(request,("usename already taken"))
            return redirect('register')

        user =User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        login(request,user)

        return redirect('Home')

    else:
        return render(request,"register.html",{})



def send_mail(request):
    send_email_to_client()


def search_result(request):
    search=request.GET.get('search')
    user=User.objects.filter(username=search)
    if user.exists():

        return redirect('/?example_param=' + search)

    else:
        return redirect('Home')
