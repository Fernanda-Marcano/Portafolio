from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name':name, 
            'email':email, 
            'message': message
        })
        
        mail = EmailMessage(
            subject, 
            template, 
            settings.EMAIL_HOST_USER,
            ['marcanoluisafernanda@gmail.com']
        )
        
        mail.fail_silently = False
        mail.send()
        
        messages.success(request, 'Se ha enviado su correo.')
        return redirect(to='index')