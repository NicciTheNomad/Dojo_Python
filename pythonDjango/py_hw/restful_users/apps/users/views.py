from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    context = {
        "all_users": User.objects.all(),
    }
    return render(request, "users/index.html", context)

def new(request):
    return render(request, "users/new.html")   

def edit(request,user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }     
    return render(request, "users/edit.html", context)

def create(request):
    result = User.objects.validate(request.POST)
    if result[0] == False:
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
    else:
        for error in result[1]:
            messages.error(request, error)
    return redirect("/users/new")

def show(request, user_id):
    context = {
        "user": User.objects.get(id=user_id),
    }        
    return render(request, "users/show.html", context)

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect ("/users")

def update(request, user_id):
    user = User.objects.get(id=user_id)
    user.first_name = request.POST["first_name"]
    user.last_name = request.POST["last_name"]
    user.email = request.POST["email"]
    user.save()
    return redirect("/users")    

