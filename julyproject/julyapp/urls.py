from django.contrib import admin
from django.urls import path, include
from . import views
from . views import ProductCreateView,ProductContactView,ProductView, ProductUpdateView, ProductDeleteView



urlpatterns = [
    path('view/', ProductCreateView.as_view(), name='view'),
    path('contact/',ProductContactView.as_view(), name='contact'),
    path("table/",ProductView.as_view(), name="table"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="delete"),
    path("company/", views.company, name="company"), 
    path("services/", views.services, name="services"), 
   
   
]
