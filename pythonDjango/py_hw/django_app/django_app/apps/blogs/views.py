from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Blog

def index(request):
    display = "demo display via HttpRes."
    return HttpResponse(display)

def new(request):
    display = "demo display NEW via HttpRes."
    return HttpResponse(display)    

def create(request):
    return redirect('/')

def display(request):
    return redirect('/')    

def show(request, user_id):
    return render(request, "blogs/show.html")

def edit(request, user_id):
    return render(request, "blogs/edit.html")

def delete(request, user_id):
    return redirect("/")        



# Create your views here.
