"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# myproject/urls.py
# myproject/urls.py
# myproject/urls.py

# myproject/urls.py

# myapp/urls.py

# # myapp/urls.py
#
# from django.contrib import admin
# from django.urls import path
# from myapp import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('orders_in_production/', views.orders_in_production, name='orders_in_production'),
#     path('customer_orders/', views.customer_orders, name='customer_orders'),
#     path('contract_summary/', views.contract_summary, name='contract_summary'),
#     path('add_address/', views.add_address, name='add_address'),
#     path('add_company/', views.add_company, name='add_company'),
#     path('add_manager/', views.add_manager, name='add_manager'),
#     path('add_customer/', views.add_customer, name='add_customer'),
#     path('add_contract/', views.add_contract, name='add_contract'),
#     path('add_order/', views.add_order, name='add_order'),
#     path('add_ad_product_type/', views.add_ad_product_type, name='add_ad_product_type'),  # Используем корректное имя
#     path('add_ad_product/', views.add_ad_product, name='add_ad_product'),
#     path('add_template/', views.add_template, name='add_template'),
#     path('add_work_act/', views.add_work_act, name='add_work_act'),
# ]

from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('orders_in_production/', views.orders_in_production, name='orders_in_production'),
    path('customer_orders/', views.customer_orders, name='customer_orders'),
    path('contract_summary/', views.contract_summary, name='contract_summary'),
    path('add_address/', views.add_address, name='add_address'),
    path('add_company/', views.add_company, name='add_company'),
    path('add_manager/', views.add_manager, name='add_manager'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_contract/', views.add_contract, name='add_contract'),
    path('add_order/', views.add_order, name='add_order'),
    path('add_ad_product_type/', views.add_ad_product_type, name='add_ad_product_type'),  # Используем корректное имя
    path('add_ad_product/', views.add_ad_product, name='add_ad_product'),
    path('add_template/', views.add_template, name='add_template'),
    path('add_work_act/', views.add_work_act, name='add_work_act'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



