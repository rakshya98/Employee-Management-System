from django.shortcuts import render, HttpResponse
from . models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    # print(context)
    return render(request, 'view_all_emp.html',context)

def add_emp(request):
    departs =Department.objects.all()
    roles=Role.objects.all()
    context = {
        'departs' : departs,
        'roles': roles
    }

    if request.method == 'POST':
        emp = Employee(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        depart = int(request.POST['depart'])
        role = int(request.POST['role'])
        new_emp=Employee(Emp_first_name=first_name,Emp_last_name=last_name,Emp_Salary=salary,Emp_bonus=bonus,Emp_phone=phone,Emp_Depart_id=depart,Emp_role_id=role,Emp_hire_date=datetime.now())
        new_emp.save()
        return render(request,'index.html')

    elif request.method=='GET':
        return render(request, 'add_emp.html',context)
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added.")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        
        except:
            return HttpResponse("Invalid")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        depart = request.POST['depart']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(Emp_first_name__icontains = name) | Q(Emp_last_name__icontains = name))  
        if depart:
            emps=emps.filter(Emp_Depart__Depart_name__icontains=depart)  
        if role:
            emps=emps.filter(Emp_role__Role_name__icontains=role)

        context = {
            'emps': emps
        } 
        return render(request, 'view_all_emp.html', context)

    elif request.method =='GET':
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse('An Exception Occured.')
