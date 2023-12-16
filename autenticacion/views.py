from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Retringir paginas
from django.contrib.auth.decorators import login_required


# Create your views here.

# Vista para crear nuevo usuario
def registrar(request):
    if request.method == "GET":
        return render(request, "registro/registro.html")
    
    if request.POST['password'] == request.POST['password2']:
        try:
            # Utiliza create_user para manejar la contraseña de manera segura
            username = request.POST['username']
            password = request.POST['password']
            name = request.POST['name']
            last_name = request.POST['last_name']
            
            user = User.objects.create_user(
                username=username, 
                password=password,
                first_name= name,
                last_name=last_name)
            
            return HttpResponse("Usuario Creado")
        
        except Exception as error:
            return HttpResponse(f"Error: {error}")
    else:
        return render(request, "registro/registro.html", {"error": "Las contraseñas no coinciden"})
        
# Vitas para iniciar sesion
def iniciarSesion(request):
    if request.method == "POST":
        arg_username = request.POST['username']
        password = request.POST['password']

        print(f"Intento de inicio de sesión: Usuario: {arg_username}, Contraseña: {password}")

        # Verificar manualmente si las credenciales son correctas
        user = authenticate(username=arg_username, password=password)

        print(f"Resultado de la autenticación: {user}")

        if user is not None and user.is_active:
            # Autenticación exitosa
            login(request, user)
            print("Inicio de sesión exitoso")
            return redirect("home")
        else:
            # Credenciales inválidas o usuario desactivado, manejar el error
            print("Inicio de sesión fallido")
            return render(request, "login/login.html", {"error": "Contraseña o usuario incorrecto"})

    return render(request, "login/login.html")


# Vista de salir sesion
def cerrarSesion(request):
    logout(request)
    return redirect("iniciarSesion")


# Vista de home
@login_required
def home(request):
    return render(request, "home_2.html")



