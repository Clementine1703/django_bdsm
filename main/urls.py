from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,  name='index'),
    path('rooms', views.rooms,  name='rooms'),
    path('rules', views.rules,  name='rules'),
    path('contacts', views.contacts,  name='contacts'),
    path('stocks', views.stocks, name='stocks'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
