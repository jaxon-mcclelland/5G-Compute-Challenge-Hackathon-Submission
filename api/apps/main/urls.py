from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r'^$', views.index),
    url(r'^csrf$', views.csrf),
]