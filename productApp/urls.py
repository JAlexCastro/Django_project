from django.urls import path
from productApp.views import vCreateProduct, vProductList, vEmail, vProductView, vProductUpdate, vProductDelete
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path("", login_required(vProductList.productList), name="productList"),
    path("create",login_required(vCreateProduct.crear_producto), name="productCreate"),
    path("email/", login_required(vEmail.send_email), name="email"),
    path("view/", login_required(vProductView.productView), name="productView"),
    path("update/", login_required(vProductUpdate.productUpdate), name="productUpdate"),
    path("delete/", login_required(vProductDelete.productDelete), name="productDelete"),

]
