from django.contrib import admin

from .models import Newsletteruser
class Newsletteradmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')
admin.site.register(Newsletteruser, Newsletteradmin )