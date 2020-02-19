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

x=0
def Residential(request):
    user = residential()
    user.type = request.POST['type']
    user.save()

  

    return render(request,'TokenNumber.html',context)


