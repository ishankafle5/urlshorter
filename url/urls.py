from django.urls import path

from url.views import *
app_name = 'urlapp'
urlpatterns = [
    path('url-short', indexpage),
    path('', indexpage),
    path('link/<str:value>', shorturl, name='shortcut')
]
