import imp
from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from .models import student

def index(request):
    stu_data=student.objects.all()
    return render(request,"index.html",{'stu_data':stu_data})


def add(request):
    if request.method=="POST":
        # retrive user input
        std_name=request.POST.get("name")
        std_roll=request.POST.get("roll")
        std_city=request.POST.get("city")
        
    # creat an object for model 
        s=student()
        s.name=std_name
        s.roll=std_roll
        s.city=std_city
        s.save()
        return redirect("home")
    return render(request,"form.html")


def delete_stu(request,id):
     print(id)
     s=student.objects.get(pk=id)
     print(s)
     s.delete()
     return redirect("home")
 
def update_stu(request,id):
    print("hello")
    stu_data=student.objects.get(pk=id)
    return render(request,"update.html",{'stu_data':stu_data})
def do_update(request,id):
    stu_name=request.POST.get("name")
    stu_roll=request.POST.get("roll")
    stu_city=request.POST.get("city")
    
    stu=student.objects.get(pk=id)
    
    stu.name=stu_name
    stu.roll=stu_roll
    stu.city=stu_city
    
    stu.save()
    return redirect("home")