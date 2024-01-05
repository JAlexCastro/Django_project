from django.shortcuts import render, redirect
from ..models import Product

# Create your views here.
def productDelete(request):

    if request.method == "POST":

        code = request.POST.get('code')
    
        
        try:
            product = Product.objects.get(codigo=code)
            product.delete()
            print(f"Producto {code} Eliminado.")

            mensaje_exito = f"Se ha Eliminado el producto."
            return render(request, 'home.html', {"mensaje_exito": mensaje_exito})
            

        except Product.DoesNotExist:
            print("Producto no existe")
            return redirect('productUpdate')

    return render(request, "productDelete.html")



