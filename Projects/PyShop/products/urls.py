from django.urls import path
from . import views

urlpatterns = [
path('', views.index), # the root of the app "/products"
path('new', views.new),
]