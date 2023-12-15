from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View


from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required,user_passes_test


# Create your views here.

def registrar(request):

    if request.method == "GET":
        return render(request, "registro/registro.html")
    
    else:
        if request.method == "POST":
            if request.POST['password'] == request.POST['password2']:
                try:
                    user = User.objects.create(

                    username=request.POST['username'],
                    first_name=request.POST['nombre'],
                    last_name=request.POST['apellido'],
                    password=request.POST['password'])

                    user.save()
                    
                    return HttpResponse("Usuario Creado ")
                
                except Exception as error:
                    return HttpResponse(f"Error:  {error}")
            else:
                return render(request, "registro/registro.html",
                              {"error": "Las contraseñas no coinciden"})

                            
def iniciarSesion(request):


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User = get_user_model()
        user = User.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            # Autenticación exitosa
            login(request, user)
            return redirect("home")
        
        else:
            return render(request, "login/login.html",  
                          {"error": "Contraseña o usuario incorrecto"})
                
    return render(request, "login/login.html")
    

def cerrarSesion(request):
    logout(request)
    return redirect("iniciarSesion")



@login_required
def home(request):
    return render(request, "home_2.html")