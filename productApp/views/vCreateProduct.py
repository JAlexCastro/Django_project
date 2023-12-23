from django.shortcuts import render, redirect
from .. import models


def crear_producto(request):

    if request.method == 'POST':
        # Capturar los datos manualmente
        codigo = request.POST.get('code')
        nombre_producto = request.POST['productName']
        precio = request.POST['productPrice']
        stock = request.POST['productStock']
        descripcion = request.POST['productDescription']
        img_producto = request.FILES.get('productImage', None)



        # Almacenar información, si el objeto no existe.
        if codigo:
            product, created = models.Product.objects.get_or_create(
                codigo=codigo,
                defaults={
                    'nombre_producto': nombre_producto,
                    'precio': precio,
                    'stock': stock,
                    'descripcion': descripcion,
                    'img_producto': img_producto
                }
            )

            if not created:
                # Si el objeto ya existía, se maneja la excepción.
                error = f"El producto con código {codigo} ya existe en la base de datos."
                print(error)
                return render(request, 'productCreate.html', {"error":error})

            
            return redirect('enviar_email', codigo)
            
        else:
            print("------Errores de formulario:")
            error = "No se pudo almacenar el producto."
            return render(request, 'productCreate.html', {"error":error})
                
    return render(request, 'productCreate.html')

