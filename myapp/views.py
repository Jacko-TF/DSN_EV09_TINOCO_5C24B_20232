from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout as user_logout

# Create your views here.

def login_form(request):
    return render(request, "login.html")

def logueo(request):
    user = authenticate(request,username=(request.POST['username']), password=(request.POST['password']))
    if user:
        login(request,user)
        return HttpResponseRedirect('home')
    else:
        return HttpResponseRedirect('login')

@login_required(login_url="/login")
def logout(request):
    user_logout(request)
    return render(request, "login.html")

def registro(request):
    return render(request, "registro.html")

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    pwd = request.POST['password']
    user = User.objects.create_user(username, email, pwd)
    user.save()
    if(User.objects.filter(username=username, email = email, password=pwd).exists()):
        return HttpResponseRedirect('home')
    else:
        return HttpResponseRedirect('login')

@login_required(login_url="/login")
def home(request):
    return render(request, "home.html")