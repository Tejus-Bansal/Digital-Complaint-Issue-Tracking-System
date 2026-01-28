from django.shortcuts import render,redirect
from complaint.models import *
from django.contrib import messages

# Create your views here.

def complaint(request):
    if request.method == 'POST':
        data = request.POST
        full_name = data.get('full_name')
        email = data.get('email')
        department_obj = Department.objects.get(id = data.get('department'))
        category_obj = Complaint_Category.objects.get(id = data.get('category'))
        description = data.get('description')
        attachment = request.FILES.get('attachment')

        Complaint.objects.create(
            user = request.user,
            full_name = full_name,
            email = email,
            department = department_obj,
            category = category_obj,
            description = description,
            attachment = attachment 
        )

        messages.success(
            request, f"Complaint registered successfully! Your Complaint ID is {complaint.complaint_id}"
        )

        return redirect('home')
    
    departments = Department.objects.all()
    categories = Complaint_Category.objects.all()
    context = {'departments': departments, 'categories': categories}
    return render(request, 'complaint/complaint_form.html', context)