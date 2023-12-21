from django.urls import path
from productApp.views import vCreateProduct, vProductList
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path("", login_required(vProductList.productList), name="productList"),
    path("create",login_required(vCreateProduct.crear_producto), name="productCreate"),

]
