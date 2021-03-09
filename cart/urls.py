from django.urls import path
from . import views
app_name = 'paiyement'
urlpatterns = [
    path('cart/',views.shopcart,name='cart'),
    
    path('delete_shopcart/<int:id>',views.delete_shopcart_item,name='delete_shopcart_item'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
   
   
]