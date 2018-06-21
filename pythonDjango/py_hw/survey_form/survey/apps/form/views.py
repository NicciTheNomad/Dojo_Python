from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    if not "tries" in request.session:
        request.session["tries"] = 0
    else:
        request.session['tries'] += 1    
    return render(request, "form/index.html")

def process(request):
    result = User.objects.validate_data(request.POST)
    if result[0] == False:
        user = User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],language=request.POST['language'], location=request.POST['location'], comment=request.POST['comment'])
    else:
        for error in result[1]:
            messages.error(request, error)
    return redirect("/display/"+ str(user.id))  

def display(request, user_id):
    context = {
        "user": User.objects.get(id=user_id), 
    }
    print context['user'].__dict__
    return render(request, 'form/result.html', context) 
            

# def display(request, user_id):
#     if request.method == "POST":
#         user = User.objects.get(id=user_id)
#         user.fname = request.POST['fname']
#         user.lname = request.POST['lname']
#         user.location = request.POST['location']
#         user.language = request.POST['language']
#         user.comment = request.POST['comment']
#         return redirect("/")
#     else:
#         context = {
#             "user": User.objects.get(id=user_id),
#         }   
#         return render(request, 'form/result.html', context)        
