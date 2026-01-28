from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def staff_dashboard(request):
    if request.user.role != 'staff':
        return redirect('home')
    return render(request, 'staff_dashboard/staff_dashboard.html')