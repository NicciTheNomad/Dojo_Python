from __future__ import unicode_literals
import string
from django.shortcuts import render, redirect
import random
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not "count" in request.session:
        request.session["count"] = 1
    # else:
    #     request.sesion["count"] = request.session["count"] + 1    
    context = {
        "randish": get_random_string(length=14),
    }
    return render(request, 'main/index.html', context)

def create(request):
    request.session["count"] = request.session["count"] + 1
    context = {
        "randish": get_random_string(length=14),
    }
    return render(request, 'main/index.html', context)  

def reset(request):
    del request.session['count']
    return redirect('/')      