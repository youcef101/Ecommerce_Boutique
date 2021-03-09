from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path('product_detail/<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    
    path('category_product/<int:id>/<slug:slug>',views.category_product,name='category_product'),
    path('addcomment/<int:id>/',views.addComment,name='addcomment'),
    path('about/',views.about,name='aboutus'),
    path('addtoshopcart/<int:id>',views.addtoshopcart,name='addtoshopcart'),
   
]