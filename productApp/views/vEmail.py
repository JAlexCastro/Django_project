from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages


# Create your views here.
def send_email1(request):
    return render(request, "contacto.html")

def send_email(request):

    if request.method == "POST":

        nombre = request.POST['nombre']
        email = request.POST['email']
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']

        template = render_to_string('email_template.html', {'nombre':nombre, 
                                                            'email':email,
                                                            'mensaje':mensaje
                                                            })

        email = EmailMessage(
            asunto,
            template,
            settings.EMAIL_HOST_USER,
            ['josenovato0@gmail.com']
        )

        # Para que no marque un error en el email
        email.fail_silently = False
        
        # Enviar email
        email.send()
        # Después de crear el producto con éxito
        mensaje_exito = f"Se ha enviaso tu correo a {nombre}"
        return render(request, 'productCreate.html', {"mensaje_exito": mensaje_exito})
    
        messages.success(request, "Se ha enviaso tu correo")
        return redirect("home")
    
    return render(request, "contacto.html")