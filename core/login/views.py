from django.shortcuts import render,redirect
from login.models import *
from django.contrib.auth import authenticate, login
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )

        if user is not None:
            login(request, user)
            print("ROLE ==> ", user.role)
            if user.role == 'staff':
                return redirect('/staff-dashboard/')
            else:
                return redirect('/client-dashboard/')
        else:
            return render(request, 'login/invalid_login_form.html', context={'error': 'Invalid Login Credentials!'})
            
    return render(request, 'login/login_form.html')