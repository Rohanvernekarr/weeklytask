from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Contactform,studentform,RegisterForm
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task

list1=[
    {"title": "title1", "text":"card-1text","price":"us$100"},
    {"title": "title2", "text":"card-2text","price":"us$200"},
    {"title": "title3", "text":"card-3text","price":"us$300"}
]

list2=[
    {"content":"hi"}
]

def firstpageview(request):
    return render(request,'first.html', {'li':list1})

def landingpageview(request):
    return render(request,'landing.html')

def pricingpageview(request):
    return render(request,'pricing.html')

def contactpage(request):
    form=Contactform()
    if request.method =='POST':
        form = Contactform(request.POST)
        if form.is_valid():
            print("Hi")
            messages.success(request,"response recorded")
            return render(request,'contact.html',{'form_data':form})
        else:
            print("bye")
            return render(request,'contact.html',{'form_data':form})
    return render(request,'contact.html',{'form_data':form})

def pricingpageview2(request):
    return render(request,'pricing2.html',{"item":list1,"con":list2})

def indexpageview(request):
    return render(request,'index.html')

def studentview(request):
    if request.method == 'POST':
        student_form = studentform(request.POST)
        if student_form.is_valid():
            student_form.save()
            print("saved")
            return redirect('success_url')  # Replace with actual URL name or path
        else:
            print("nop")
    else:
        student_form = studentform()

    return render(request, 'student.html', {'student_data': student_form})

@ensure_csrf_cookie
def registerview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user to database
            print(f"User created: {user.username}")  # Debug print
            messages.success(request, "Registration successful! Please login.")
            return redirect('login')
        else:
            print(f"Form errors: {form.errors}")  # Debug print
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def loginview(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid username or password.'
    return render(request, 'login.html', {'error': error})

def logoutview(request):
    logout(request)
    return redirect('home')

#DASHBOARD PAGE

@login_required
def dashboardview(request):
    return render(request,'dashboard.html')

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer







