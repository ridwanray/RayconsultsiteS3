#from .forms import Contactform
#from django.urls import reverse
#from django.http import  HttpResponseRedirect
#from .models import Contact

#from operator import attrgetter
#from itertools import chain
from django.shortcuts import render
from .models import Blog


def blog_list(request):
	bloglistings= Blog.objects.all().order_by('date')[:12]
	return render(request, 'article/article_list.html', {'bloglistings':bloglistings})

def blog_detail(request,slug):
	blogdetails= Blog.objects.get(slug=slug)
	return render(request, 'article/article_detail.html', {'blogdetails': blogdetails})


#travels= Travel.objects.all().order_by('-date')
#nutritions= Nutrition.objects.all().order_by('-date')
#sports= Sport.objects.all().order_by('-date')
#def Contactview(request):
#    if request.method == 'POST':
##       if form.is_valid():
  #          name=request.POST.get('name', '')
   ###       email=request.POST.get('email', '')
#            detail=Contact(name= name, subject= subject, email= email, content= content)
#            detail.save()
##
 #           HttpResponseRedirect(reverse('contact'))
 #       else:
  #          form= Contactform()

   #     return render(request, 'template/contact.html', {'form':form})



#def sport_list(request):
#    travels= Travel.objects.all().order_by('-date')
#    nutritions= Nutrition.objects.all().order_by('-date')
#    sports= Sport.objects.all().order_by('-date')
#
#    sportas = sorted(
#        chain(travels, nutritions, sports),
#        key = attrgetter('date'), reverse=True)[:24]
#    return render(request, 'sport/sport_list.html', {'sportas':sportas})
#
#
#
#def sport_detail(request,slug):
#    travels= Travel.objects.all()
#    nutritions= Nutrition.objects.all()
#    sports= Sport.objects.all()
#
#    newa = sorted(
#        chain(travels, nutritions, sports),
#        key = attrgetter('date'), reverse=True)[:24]
#    sportas=newa.objects.get(slug)
#
#    return render(request, 'sport/sport_detail.html', {'sportas':sportas})


def sport_list(request):
	sports= Sport.objects.all().order_by('date')[:12]
	return render(request, 'sport/sport_list.html', {'sports':sports})

def sport_detail(request,slug):
	sportdetail= Sport.objects.get(slug=slug)
	return render(request, 'sport/sport_detail.html', {'sportdetail': sportdetail})





#def travel_list(request):
#	travels= Travel.objects.all().order_by('date')[:12]
#	return render(request, 'travel/travel_list.html', {'travels':travels})
#
#def travel_detail(request,slug):
#	traveldetail= Travel.objects.get(slug=slug)
#
#
#def lifestyle_list(request):
#	lifestyles= lifestyle.objects.all().order_by('date')[:12]
#	return render(request, 'lifestyle/lifestyle_list.html', {'lifestyles':lifestyles})
#
#def nutrition_list(request):
#	nutritions= Nutrition.objects.all().order_by('date')[:12]
#	return render(request, 'nutrition/nutrition_list.html', {'nutritions':nutritions})

#def health_list(request):
#	healths= Health.objects.all().order_by('date')[:12]
#	return render(request, 'health/health_list.html', {'healths':healths})
#
#def agriculture_list(request):
#	agricultures= Agriculture.objects.all().order_by('date')[:12]
#	return render(request, 'agriculture/agriculture_list.html', {'agricultures':agricultures})
##
#def hardware_list(request):
#	hardwares= Hardware.objects.all().order_by('date')[:12]
#	return render(request, 'hardware/hardware_list.html', {'hardwares':hardwares})

#def programming_list(request):
#	programmings= Programming.objects.all().order_by('date')[:12]
#	return render(request, 'programming/programming_list.html', {'programmings':programmings})

#def software_list(request):
##	return render(request, 'software/software_list.html', {'softwares':softwares})


#def networking_list(request):
#	networkings= Networking.objects.all().order_by('date')[:12]
#	return render(request, 'networking/networking_list.html', {'networkings':networkings})


#def politics_list(request):
#	politicss= Politics.objects.all().order_by('date')[:12]
#	return render(request, 'politics/politics_list.html', {'politicss':politicss})


#def education_list(request):
#	educations= Education.objects.all().order_by('date')[:12]
#	return render(request, 'education/education_list.html', {'educations':educations})

#def business_list(request):
#	businesss= Business.objects.all().order_by('date')[:12]
#	return render(request, 'business/business_list.html', {'businesss':businesss})

#def politics_detail(request,slug):

#	politicsdetail = Politics.objects.get(slug=slug)
#	return render(request, 'politics/politics_detail.html', {'politicsdetail': politicsdetail})

#def programming_detail(request,slug):

#	programmingdetail = Programming.objects.get(slug=slug)
#	return render(request, 'programming/programming_detail.html', {'programmingdetail': programmingdetail})

#def agriculture_detail(request,slug):

#	return render(request, 'agriculture/agriculture_detail.html', {'agriculturedetail': agriculturedetail})

#def education_detail(request,slug):

#	educationdetail= Education.objects.get(slug=slug)
#	return render(request, 'education/education_detail.html', {'educationdetail': educationdetail})
#def hardware_detail(request,slug):

#	hardwaredetail = Hardware.objects.get(slug=slug)
#	return render(request, 'hardware/hardware_detail.html', {'hardwaredetail': hardwaredetail})


#def lifestyle_detail(request,slug):

#	return render(request, 'lifestyle/lifestyle_detail.html', {'lifestyledetail': lifestyledetail})

##def networking_detail(request,slug):

#	networkingdetail = Networking.objects.get(slug=slug)
#	return render(request, 'networking/networking_detail.html', {'networkingdetail': networkingdetail})


#def business_detail(request,slug):
#	businessdetail = Business.objects.get(slug=slug)
#	return render(request, 'business/business_detail.html', {'businessdetail':businessdetail})

"""
----multiline comment
def health_detail(request,slug):
healthdetail = Health.objects.get(slug=slug)
	return render(request, 'health/health_detail.html', {'healthdetail': healthdetail})

def nutrition_detail(request,slug):

	nutritiondetail = Nutrition.objects.get(slug=slug)
	return render(request, 'sport/sport_detail.html', {'nutritiondetail': nutritiondetail})




def software_detail(request,slug):

	softwaredetail= Software.objects.get(slug=slug)
	return render(request, 'software/software_detail.html', {'softwaredetail': softwaredetail})

---multiline comment
"""