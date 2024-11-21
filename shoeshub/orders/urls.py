from django.urls import path
from . import views




urlpatterns = [

    path('show_cart',views.show_cart,name='show_cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<id>',views.remove_item,name='remove_item'),
    path('checkout_cart',views.checkout_cart,name='checkout_cart'),
    path('view_orders',views.view_orders,name='view_orders'),
    # path('payment',views.payment,name='payment'),
    # path('sucess',views.sucess,name='sucess'),

   
 ]