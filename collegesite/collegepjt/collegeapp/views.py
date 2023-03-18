from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import department
from.models import courses
# Create your views here.
def index(request):
    return render(request,"index.html")

def computer(request):
    return render(request,"computer.html")

def commerce(request):
    return render(request,"commerce.html")

def maths(request):
    return render(request,"maths.html")

def science(request):
    return render(request,"science.html")

def home(request):
    return render(request,"index.html")

def portfolio(request):
    return render(request,"portfolio.html")

def details(request):
    dept=department.objects.all()

    return render(request,"details.html",{'depart':dept})

def load_courses(request):
    department_id = request.GET.get('department')
    course = courses.objects.filter(dept_id=department_id)
    for i in course:
        print(i)
    return render(request,'course_list.html',{'courses': course})


def order(request):
    msg=messages.info(request,"Order Confirmed")
    return redirect('details')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('portfolio')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']

        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request," Username already taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request," Password mismatch")
            return redirect("register")
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')