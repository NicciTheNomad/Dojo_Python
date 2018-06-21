from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from .models import Message
from .models import *

# Create your views here.
#posts
def index(request):
    return render(request, "posts/index.html")

def new(request):
    return render(request, "posts/new.html")

def edit(request):
    return render(request, "posts/edit.html")          

# show or update later
def show(request): 
    context = {
        "message": Message.objects.get(id=1).content,
        # "comment": Comment.objects.filter(message=Message.objects.get(id=1)).values('comment'),
        "comment": Comment.objects.filter(message=Message.objects.get(id=1)).values("comment"),
        "comment_b": Comment.objects.get(id=1).comment,
        # "message": Message.objects.get(id=message_id),
        # "comment": Comment.objects.get(id=comment_id),
    }      
    return render(request, "posts/show.html", context) 
