from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, "user_login/index.html")

def process(request):
    if request.method == "POST":
        result = User.objects.validate(request.POST)
        if result[0] == False:
            User.objects.create(fname=request.POST["fname"],lname=request.POST["lname"],age=request.POST["age"],email=request.POST["email"])
        else:
            for error in result[1]:
                messages.error(request, error)
        return redirect("/")

def display(request):
    context = {
        "all_users":User.objects.all(),
    }
    return render(request, "user_login/show.html", context)
