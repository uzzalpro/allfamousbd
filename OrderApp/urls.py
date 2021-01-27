from django.urls import path
from OrderApp.views import Add_to_Shoping_cart,cart_details,cart_delete,OrderCart,Order_showing,Order_Product_showing,user_order_details,user_order_product_details



urlpatterns = [
    path('addingcart/<int:id>', Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
    path('cart_details/', cart_details, name='cart_details'),
    path('cart_delete/<int:id>', cart_delete, name='cart_delete'),
    path('order_cart/', OrderCart, name='OrderCart'),
    path('orderlist/', Order_showing, name='orderlist'),
    path('OrderProduct/', Order_Product_showing, name='OrderProduct'),
    path('order_details/<int:id>', user_order_details, name='user_order_details'),
    path('userorderproductdetails/<int:id>/<int:oid>', user_order_product_details, name='user_order_product_details')
]