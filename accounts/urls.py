from django.urls import path
from .import views
app_name = 'accounts'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('user_comment/',views.user_comment,name='user_comment'),
    path('delete_comment/<int:id>/',views.delete_comment,name='delete_comment'),
    path('user_order/',views.user_orders,name='user_order'),
    path('orderdetail/<int:id>', views.user_orders_detail, name='user_order_detail'),
    path('orders_product/', views.user_orders_product, name='user_order_product'),
    path('order_product_detail/<int:id>/<int:oid>', views.user_orders_product_detail, name='user_order_product_detail'),
]