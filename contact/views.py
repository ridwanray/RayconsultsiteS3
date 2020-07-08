from django.shortcuts import render
from .models import Contact
def contactview(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        content=request.POST.get('content')
        newone = Contact(name=name,email=email,subject=subject,content=content)
        newone.save()
        return render(request, 'contact/success.html', {})
    else:
        return render(request, 'contact/contact.html', {})

def handler404(request):
    return render(request, 'contact/404.html', status=404)








