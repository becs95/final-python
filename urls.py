from django.urls import path
from .import views

def new_func():
    return path("pro_gol/",views.pro_gol, name="pro_gol")

urlpatterns = [
    new_func()
]
