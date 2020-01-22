from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^key', views.Key, name='key'),
    url(r'^', views.index, name='key-form'),
]
