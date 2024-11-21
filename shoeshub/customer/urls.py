from django.urls import path
from . import views




urlpatterns = [

    path('show_account',views.show_account,name='show_account'),
    path('signout',views.signout,name='signout'),
    
 ]