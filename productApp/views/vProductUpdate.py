from django.shortcuts import render, redirect
from ..models import Product

# Create your views here.
def productUpdate(request):

    if request.method == "POST":

        code = request.POST.get('code')
        productName = request.POST.get('productName')
        productPrice = request.POST.get('productPrice')
        productStock = request.POST.get('productStock')
        productDescription = request.POST.get('productDescription')
        
        try:
            product = Product.objects.get(codigo=code)
            product.nombre_producto = productName
            product.precio = productPrice
            product.stock = productStock
            product.descripcion = productDescription
            product.save()
            print("Producto actualizado.")

            mensaje_exito = f"Se ha actualizado el producto."
            return render(request, 'home.html', {"mensaje_exito": mensaje_exito})
            

        except Product.DoesNotExist:
            print("Producto no existe")
            return redirect('productUpdate')

    return render(request, "productUpdate.html")



