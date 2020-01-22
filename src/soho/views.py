from django.shortcuts import render


# Create your views here.
from .models import soho


def index(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [1, 2, 3],
    }
    print(args, kwargs)
    print(request)
    return render(request, "SOHOM.html", my_context)


def Soho(request):
    user = soho()
    user.type = request.POST['type']
    user.save()

    print(user.type)

    if user.type == 'AIRO-net':
        return render(request, 'airo_net.html')
    elif user.type == 'School-net':
        return render(request, 'school_net.html')
    elif user.type == 'VSAT':
        return render(request, 'vsat.html')
    return render(request, "Hybrid.html")
