from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login

def auth_staff(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)

        else:
            # Return a 'disabled account' error message

    else:
        # Return an 'invalid login' error message.

