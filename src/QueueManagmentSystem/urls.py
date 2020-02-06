"""QueueManagmentSystem URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from pages.views import  welcome_view
from pages.views import generatenumber_view




urlpatterns = [
    path('', home_view),
    path('home/', home_view),
    path('registerForm/', include('RegisterForm.urls')),
    path('residential/', include('residential.urls')),
    path('Enterprise/', include('Enterprise.urls')),
    path('keyAccount/', include("key.urls")),
    path('soho/', include('soho.urls')),
    path('welcome/',welcome_view),
    path('generatenumber/',generatenumber_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)