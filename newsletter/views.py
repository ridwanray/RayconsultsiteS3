from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from .models import Newsletteruser
from .forms import Newslettersignupform



def newsletter_unsubscribe(request):
    form = Newslettersignupform(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Newsletteruser.objects.filter(email=instance.email).exists():
            Newsletteruser.objects.filter(email=instance.email).delete()
            messages.success(request,
                                'Your Email Has Been Removed!',
                                 "alert alert-success")
            subject = "You have been unsubscribe"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/rayup/hotels/newsletter/templates/newsletter/unsubscribe_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletter/unsubscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
        else:

            messages.warning(request,
                                'Your Email Is Not In The Database!',
                                "alert alert-warning")
    return render(request, 'newsletter/unsubscribe.html', {'form':form})



def newsletter_signup(request):
    form = Newslettersignupform(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Newsletteruser.objects.filter(email=instance.email).exists():
            messages.warning(request,


                                'Your Email Already Exists In Our Database!',
                                "alert alert-warning")
        else:
            instance.save()
            messages.success(request,
                                'Your Email Has Been Submitted To The Database!',
                                 "alert alert-success")
            subject = "Thank You For Joining Our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/rayup/hotels/newsletter/templates/newsletter/sign_up_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletter/sign_up_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()


    return render(request, 'newsletter/subscribe.html', {'form':form})

