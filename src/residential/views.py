from django.shortcuts import render


# Create your views here.
from .models import residential


def index(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [1, 2, 3],
    }
    print(args, kwargs)
    print(request)
    return render(request, "residential.html", my_context)


def Residential(request):
    user = residential()
    user.type = request.POST['type']
    user.save()

    print(user.type)

    if user.type == 'Business_Mobile':
        return render(request, 'Business_Mobile.html')
    elif user.type == 'Broadband':
        return render(request, 'Broadband.html')
    elif user.type == 'Bill_Collection':
        return render(request, 'Bill_Collection.html')
    elif user.type == 'Hybrid':
        return render(request, 'Hybrid.html')
    elif user.type == "FixedLine":
        return render(request, 'FixedLine.html')
    return render(request, "Personal.html")


