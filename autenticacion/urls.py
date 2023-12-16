from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("registro/", views.registrar, name="autenticacion"),
    path("login/", views.iniciarSesion, name="iniciarSesion"),
    path("logout/", views.cerrarSesion, name="cerrarSesion"),
    #path('home/', login_required(views.home, login_url='/login/'), name='home'),
    path("home/", views.home, name="home" )
    
]
