from django.conf.urls import urls
from . import views

urlpattern = [
    url(r'^add_message$', views.add_message),
]