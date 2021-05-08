from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import EmployeeDetails


def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, 'employee_form.html', {'form': form})

    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')


def employee_list(request):
    context = EmployeeDetails.objects.all()
    return render(request, 'employee_list.html', {'context': context})

