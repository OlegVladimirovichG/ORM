from django import forms
from my_app import Product

class ProductPhotoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['photo']
