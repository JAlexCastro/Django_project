from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("head", views.home3, name="homeDos")
]
