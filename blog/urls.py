from django.conf.urls import url
from . import views
app_name='news'


urlpatterns =[
	url(r'^$', views.blog_list, name="bloglist"),
	url(r'^(?P<slug>[\w-]+)/$', views.blog_detail, name="blogdetail"),


#	url(r'^softwares/$', views.software_list, name='softwarelist'),
###	url(r'^nutritions/$', views.nutrition_list, name='nutritionlist'),
#	url(r'^healths/$', views.health_list, name='healthlist'),
#	url(r'^agricultures/$', views.agriculture_list, name='agriculturelist'),
#	url(r'^hardwares/$', views.hardware_list, name='hardwarelist'),
#	url(r'^programmings/$', views.programming_list, name='programminglist'),
#	url(r'^networkings/$', views.networking_list, name='networkinglist'),
#	url(r'^politics/$', views.politics_list, name='politicslist'),
#	url(r'^educations/$', views.education_list, name='educationlist'),
#	url(r'^businesses/$', views.business_list, name='businesslist'),
###	url(r'^software/(?P<slug>[\w-]+)/$', views.software_detail, name='softwaredetail'),
#	url(r'lifestyle/(?P<slug>[\w-]+)/$', views.lifestyle_detail, name='lifestyledetail'),
#	url(r'^nutrition/(?P<slug>[\w-]+)/$', views.nutrition_detail, name='nutritiondetail'),
#	url(r'^health/(?P<slug>[\w-]+)/$', views.health_detail, name='healthdetail'),
#	url(r'^agriculture/(?P<slug>[\w-]+)/$', views.agriculture_detail, name='agriculturedetail'),
#	url(r'^hardware/(?P<slug>[\w-]+)/$', views.hardware_detail, name='hardwaredetail'),
#	url(r'^programming/(?P<slug>[\w-]+)/$', views.programming_detail, name='programmingdetail'),
#	url(r'^networking/(?P<slug>[\w-]+)/$', views.networking_detail, name='networkingdetail'),
#	url(r'^politics/(?P<slug>[\w-]+)/$', views.politics_detail, name='politicsdetail'),
#	url(r'^education/(?P<slug>[\w-]+)/$', views.education_detail, name='educationdetail'),
#	url(r'^business/(?P<slug>[\w-]+)/$', views.business_detail, name='businessdetail'),


]
