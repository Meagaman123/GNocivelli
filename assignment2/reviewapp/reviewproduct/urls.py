from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='reviewproduct-home'),
    path('about/', views.about, name='reviewProduct-about'),
    path('contact/', views.contact, name='reviewProduct-contact'),
    path('products/', views.products, name='reviewProduct-products')
]