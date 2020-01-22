from django.shortcuts import render


# Create your views here.
from .models import enterprise


def index(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [1, 2, 3],
    }
    print(args, kwargs)
    print(request)
    return render(request, "Enterprise.html", my_context)


def Enterprise(request):
    user = enterprise()
    user.type = request.POST['type']
    user.save()

    print(user.type)

    if user.type == 'keyaccount':
        return render(request, 'keyAccount.html')
    return render(request, "SOHOM.html")


