from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^residential', views.Residential, name='residential'),
    url(r'^', views.index, name='residential-form'),
]
