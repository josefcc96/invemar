from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
urlpatterns = [
    path('', admin.site.urls),


]
#admin.site.site_header = 'Nuevo nombre'
