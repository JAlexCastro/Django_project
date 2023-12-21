from django import forms

class ProductForm(forms.Form):
    code = forms.CharField(label='Código', max_length=100)
    productName = forms.CharField(label='Nombre del producto', max_length=100)
    productPrice = forms.DecimalField(label='Precio', required=False)
    productStock = forms.DecimalField(label='Stock', required=False)
    productDescription = forms.CharField(label='Descripción', max_length=150, required=False)
    productImage = forms.ImageField(label='Imagen del producto', required=False)
