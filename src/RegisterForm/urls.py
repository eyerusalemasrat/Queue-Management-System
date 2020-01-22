from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register-user', views.register, name='register-user'),
    url(r'^', views.index, name='register-form'),
]
