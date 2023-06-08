# from pyexpat.errors import messages

from django.shortcuts import render
from django.shortcuts import redirect

from crud_operation.models import Student
from django.http import HttpResponse


# Create your views here.
def home (request):
    std=Student.objects.all()
    return render(request,"home.html",{'std':std})

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email=request.POST['email']
        phone = request.POST['phone']
        address=request.POST['address']
        new_emp = Student(first_name=first_name, last_name=last_name,phone=phone,
                          email=email,address=address)
        new_emp.save()
        return HttpResponse("<h1>student added successfully<h1>")
    elif request.method == 'GET':
        return render(request, 'add_student.html')
    else:
        return HttpResponse("<h2>error student has not been added<h2>")

def delete_student(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return HttpResponse("<h3>deleted successfully<h3>")

def update_student(request,id):
    students=Student.objects.get(id=id)
    s1= Student.objects.all()
    context={
        'students':students,
        's1': s1
    }
    return render(request, 'update.html', context)

def do_update_student(request,id):
    std=Student.objects.get(id=id)
    std.first_name=request.POST['first_name']
    std.last_name= request.POST['last_name']
    std.email=request.POST['email']
    std.phone=request.POST['phone']
    std.address=request.POST['address']
    std.save()
    return HttpResponse('updated successfully')
    return redirect('update.html')