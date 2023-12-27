from django.shortcuts import render
from ..models import Product

# Create your views here.
def productList(request):
    
    productos = Product.objects.all()[:9]
    return render(request, "productList.html", {'productos' : productos})



