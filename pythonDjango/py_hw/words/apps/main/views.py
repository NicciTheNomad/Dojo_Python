from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def process(request):
    new_word = {}
    for key, value in request.POST.iteritmes():
        if key != "csrfmiddlewaretoken" and key != "increase":
            new_word[key] = value
        if key == "increase"   
            new_word[""] 
    return redirect('/')    

def clear_session(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
