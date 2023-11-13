from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect

def send_email_to_client(request):
    subject="from celestial coders"
    message=" this is test no. 6"
    from_email=settings.EMAIL_HOST_USER
    mail="webdevmsit@gmail.com"
    recipient_list=[mail]
    send_mail(subject,message,from_email,recipient_list)
    return redirect('Home')

