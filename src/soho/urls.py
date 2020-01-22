from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^soho', views.Soho, name='soho'),
    url(r'^', views.index, name='soho-form'),
]
