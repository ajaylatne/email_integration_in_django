from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def send_mail_view(request):
    if request.method == 'POST':
        user_mail = request.POST['mail']
        user_name = request.POST['name']
        subject = 'Test mail'
        message = f'hi {user_name} ignore this mail just for testing purpose'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user_mail]
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('check your mail')
    return render(request, 'send_mail_app/mail.html')
