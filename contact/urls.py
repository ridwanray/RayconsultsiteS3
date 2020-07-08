from django.conf.urls import url
from . import views
namespace='contact'

urlpatterns =[
    url(r'^$', views.contactview, name='contactview'),
    #url(r'^success$', views.success, name='successu'),
    #url(r'^subscribe$', views.subscribe, name='subscribe'),

    ]