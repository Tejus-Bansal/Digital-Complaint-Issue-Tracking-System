from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def client_dashboard(request):
    if request.user.role != 'client':
        return redirect('home')
    return render(request, 'client_dashboard/client_dashboard.html')

