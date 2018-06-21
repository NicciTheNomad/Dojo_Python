from django.conf.urls import url
from . import views
#users
urlpatterns = [
    url(r'^$', views.index),
    url(r'new$', views.new),
    url(r'^(?P<user_id>\d+)/delete$', views.delete),
    url(r'^(?P<user_id>\d+)/edit$', views.edit),
    url(r'^(?P<user_id>\d+)', views.show_or_update),
    url(r'^(?P<user_id>\d+)', views.integrated),
]
