from django.conf.urls import url
from . import views
#posts
urlpatterns = [
    url(r'^$', views.show),
    # url(r'^messages$', views.index),
    url(r'^new$', views.new),
    url(r'^show$', views.show),
    url(r'^edit$', views.edit),
    
]
