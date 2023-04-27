from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/',obtain_auth_token,name='api-auth-token'),
    path('',views.product_create),
    path('api/',views.home,name='home'),
    path('list_create/',views.product_list_create),
    path('api/<int:pk>/',views.home,name='home'),
    path('api/product/<int:pk>/',views.product_retrieve),
    path('api/update/<int:pk>/',views.product_update_view),
    path('api/delete/<int:pk>/',views.product_delete_view),
    path('listmixin/',views.product_listmixin_view),
    path('createmixin/',views.product_createmixin_view),
    path('updatemixin/<int:pk>/',views.product_updatemixin_view),

]  