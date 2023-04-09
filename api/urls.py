from . import views
from django.urls import path

urlpatterns = [
    path('api/update/<int:pk>/',views.product_update_view),
    path('',views.product_create),
    path('api/',views.home,name='home'),
    path('list_create/',views.product_list_create),
    path('api/<int:pk>/',views.home,name='home'),
    path('api/product/<int:pk>/',views.product_retrieve),
]  