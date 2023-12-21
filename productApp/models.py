from django.db import models

# Create your models here.
class Product(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    precio = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    stock = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=150, null=True)
    img_producto = models.ImageField(upload_to="products",null=True)

    class meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f"Codigo {self.codigo} del producto {self.nombre_producto}"
