from __future__ import unicode_literals
import random
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # request.session["hello"] = "testing"
    if not "correct_number" in request.session:
        request.session["correct_number"] = random.randint(1,100)
    print request.session["correct_number"]
    context = {
        "correct_number": request.session["correct_number"]
    }
    return render(request, "main/index.html", context)
def process(request):
    request.session["guessed_number"] = int(request.POST["number"])
    return redirect('/')
def reset(request):
    request.session.clear()
    return redirect('/')   

