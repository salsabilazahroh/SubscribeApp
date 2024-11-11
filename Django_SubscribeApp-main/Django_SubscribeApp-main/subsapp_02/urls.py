from django.urls import path
from subsapp_02 import views

urlpatterns = [
    path('', views.customers, name='customers'),
    # path('customers/', views.customer_list, name='customer_list'),
]