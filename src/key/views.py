from django.shortcuts import render


# Create your views here.
from .models import key


def index(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [1, 2, 3],
    }
    print(args, kwargs)
    print(request)
    return render(request, "keyAccount.html", my_context)


def Key(request):
    user = key()
    user.type = request.POST['type']
    user.save()

    print(user.type)

    if user.type == 'M2M Business':
        return render(request, 'M2M_Business.html')
    elif user.type == 'Broadband':
        return render(request, 'Broadband.html')
    elif user.type == 'Bill Collection':
        return render(request, 'Bill_Collection.html')
    elif user.type == 'Hybrid':
        return render(request, 'Hybrid.html')
    return render(request, "GotaServices.html")


