from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(req):
    if req.method == "POST":
        User.objects.create(name=req.POST["name"],email=req.POST["email"])
        return redirect("/users/new")

    elif req.method == "GET":    
        context = {
            "all_users":User.objects.all()
        }
        return render(req, "users/index.html", context)

def land(request):
    return render(request, "users/land.html")   

def new(request):
    return render(request, "users/new.html")  

def delete(request, user_id):
    print user_id
    User.objects.get(id=user_id).delete()
    return redirect ("/users") 

def edit(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, "users/edit.html", context)     

def show_or_update(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=user_id)      
        user.name = request.POST["name"]
        user.email = request.POST["email"]
        user.save()  
        return redirect("/users")
    else:
        context = {
            "user": User.objects.get(id=user_id),
        } 
        return render(request, "users/show.html", context)   
