"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from stockmgmt import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('list_items/', views.list_items, name='list_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('add_items/', views.add_items, name='add_items'),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
    path('accounts/', include('registration.backends.default.urls')),
    path('list_customer/', views.list_customer, name='list_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<str:pk>/', views.update_customer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.delete_customer, name="delete_customer"),
    path('customer_detail/<str:pk>/', views.customer_detail, name="customer_detail"),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
    path('list_invoice/', views.list_invoice, name='list_invoice'),
    path('update_invoice/<str:pk>/', views.update_invoice, name="update_invoice"),
    path('delete_invoice/<str:pk>/', views.delete_invoice, name="delete_invoice"),
    path('invoice_detail/<str:pk>/', views.invoice_detail, name="invoice_detail"),
    path('add_daily_accounts/', views.add_daily_accounts, name ="add_daily_accounts"),
    path('list_daily_accounts/', views.list_daily_accounts, name = "list_daily_accounts"),
    path('daily_accounts_details/<str:pk>', views.daily_accounts_details, name = "daily_accounts_details"),
    path('update_daily_accounts/<str:pk>/', views.update_daily_accounts, name="update_daily_accounts"),
    path('delete_daily_accounts/<str:pk>/', views.delete_daily_accounts, name="delete_daily_accounts")
    

    

   
   

]
