from django.shortcuts import redirect, render
from register.models import *

# Create your views here.

def register(request):
    if request.method == "POST":
        data = request.POST

        firstname = data.get('firstname')
        lastname = data.get('lastname')
        username = data.get('username')
        password = data.get('password')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname,
            role='client'
        )

        Client.objects.create(user=user)

        return redirect('/login/')
    
    return render(request, 'register/registeration_form.html')