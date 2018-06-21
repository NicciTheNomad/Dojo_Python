from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
#views is the "controller"

# def index(request):
#     context = {
#         "key":"value",
#         "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#     }
#     return render(request, 'display/index.html', context)

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    context = {
        "key":"value",
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'display/index.html', context)    
