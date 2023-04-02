from . import views
from django.urls import path

urlpatterns = [
    path('api/',views.home,name='home')
]