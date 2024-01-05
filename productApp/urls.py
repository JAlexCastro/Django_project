from django.urls import path
from productApp.views import vCreateProduct, vProductList, vEmail, vProductView, vProductUpdate, vProductDelete
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path("", login_required(vProductList.productList), name="productList"),
    path("create",login_required(vCreateProduct.crear_producto), name="productCreate"),
    path("email/", vEmail.send_email, name="email"),
    path("view/", vProductView.productView, name="productView"),
    path("update/", vProductUpdate.productUpdate, name="productUpdate"),
    path("delete/", vProductDelete.productDelete, name="productDelete"),

]
