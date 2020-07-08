from django.shortcuts import render
def home(request):
    return render(request, 'homepage.html')

#def contact(request):
#    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

