from django.urls import path

from .views import index, new_url, url_redirect


urlpatterns = [
    path('', index, name='index'),
    path('new_url/<str:slug>', new_url, name='new_url'),
    path('r/<str:slug>', url_redirect, name='url_redirect')
]