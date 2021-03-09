from .models import *

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','address','zipcode','state','phone','city','country']