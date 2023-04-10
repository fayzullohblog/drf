from . import views
from django.urls import path

urlpatterns = [
    path('',views.product_create),
    path('api/',views.home,name='home'),
    path('list_create/',views.product_list_create),
    path('api/<int:pk>/',views.home,name='home'),
    path('api/product/<int:pk>/',views.product_retrieve),
    path('api/update/<int:pk>/',views.product_update_view),
    path('api/delete/<int:pk>/',views.product_delete_view),
]  