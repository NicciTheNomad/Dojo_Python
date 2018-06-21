from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index), #/ninjagold
    url(r'^hello/(?P<name>\D+)$', views.hello) #/ninjagold/hello
]
