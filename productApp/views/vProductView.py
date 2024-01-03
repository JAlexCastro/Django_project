from django.shortcuts import render
from ..models import Product

# Create your views here.
def productView(request):
    codigo = 100
    productos = Product.objects.filter(codigo=codigo)
    return render(request, "productView.html", {'productos' : productos})



