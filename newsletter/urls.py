from django.conf.urls import url
from . import views
app_name='newsletter'

urlpatterns =[
    url(r'^subscribe/$', views.newsletter_signup, name='newslettersignup'),
    url(r'^unsubscribe/$', views.newsletter_unsubscribe, name='newsletterunsubscribe'),
    ]