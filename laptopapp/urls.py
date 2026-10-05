from django.urls import path
from . import views

urlpatterns = [
    path('laptop/', views.laptop_price_predict, name='laptop_price_predict'),
]
