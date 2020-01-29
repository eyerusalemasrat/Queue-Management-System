from django.shortcuts import render

from django.contrib import messages

from django.forms import ValidationError



# Create your views here.
from .models import RegisterForm


def index(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [1, 2, 3],
    }
    print(args, kwargs)
    print(request)
    return render(request, "Register.html", my_context)


def register(request):
    user = RegisterForm()
    user.name = request.POST['name']
    user.phoneNumber = request.POST['phone_number']
    user.type = request.POST['type']

    if user.name != "" and len(user.phoneNumber) == 10:
        user.save()
        if user.type == 'residential':
            return render(request, 'Residential.html')
        return render(request, "Enterprise.html")
    else:
        return render(request, 'Register.html')
        return ValidationError('Domain of email is not valid')

        return messages.error(request, 'The form is invalid.')







