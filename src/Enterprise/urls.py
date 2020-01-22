from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^enterprise', views.Enterprise, name='enterprise'),
    url(r'^', views.index, name='enterprise-form'),
]
