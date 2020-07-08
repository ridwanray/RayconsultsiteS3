from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from cart.views import CartView, ItemCountView, CheckoutView, CheckoutFinalView
from orders.views import (
                    AddressSelectFormView,
                    UserAddressCreateView,
                    OrderList,
                    OrderDetail)

app_name='main'

urlpatterns = [
    url( 'adminrilo/', admin.site.urls),
    #url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^service/$', views.service, name='service'),
    url(r'^$', views.home, name='homepage'),
   # url(r'^blog/', include('blog.urls')),
    #url(r'^ordering/$', 'newsletter1.views.home', name='ecommercehome'),
    url(r'^contact/', include('contact.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^products/', include('shop.urls')),
    #url(r'^categories/', include('shop.urls_categories')),
    #url(r'^orders/$', OrderList.as_view(), name='orders'),
    #url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
   # url(r'^cart/$', CartView.as_view(), name='cart'),
    #url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),
    #url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    #url(r'^checkout/address/$', AddressSelectFormView.as_view(), name='order_address'),
    #url(r'^checkout/address/add/$', UserAddressCreateView.as_view(), name='user_address_create'),
    #url(r'^checkout/final/$', CheckoutFinalView.as_view(), name='checkout_final'), 
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'contact.views.handler404'
