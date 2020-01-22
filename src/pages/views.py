from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request)
    return render(request,"home.html", {})

def Residential_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"Residential.html", {})

def Enterprise_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"Enterprise.html", {})

def keyAccount_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"keyAccount.html", {})

def SOHOM_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"SOHOM.html", {})

def welcome_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"welcome.html", {})

def generatenumber_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"generateNumber.html", {})

def generatenumber_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"generateNumber.html", {})

def Bill_Collection_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"Bill_Collection.html", {})

def Broadband_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"Bill_Collection.html", {})

def Business_Mobile_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"Business_Mobile.html", {})

def FixedLine_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"FixedLine.html", {})

def Hybrid_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"Hybrid.html", {})

def Personal_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"Personal.html", {})

def GotaServices_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"GotaServices.html", {})

def M2M_Business_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request,"M2M_Business.html", {})


