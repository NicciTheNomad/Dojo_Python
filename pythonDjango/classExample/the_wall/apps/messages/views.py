from django.shortcuts import render, HttpResponse, redirect
django.contrib import messages
from .models import Message

# Create your views here.
def index(request):
    if request.method == "POST":
        Message.objects.create(name=request.POST['message'])
        return redirect("/users")#not sure where to redirect
    else:
        pass    
