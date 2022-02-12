"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app1 import views

urlpatterns = [

    ################################################# HEADER #################################################

    path('admin/', views.admin),
    path('sales/', views.sales),
    path('service/', views.service),
    path('public/', views.public),
    path('customer/', views.customer),

    ################################################# STAFF #################################################

    path('appointment/', views.appointment),
    path('appoint/', views.appoint),

    path('remove_staff/', views.remove_staff),
    path('remove_staff_functions/<int:id>', views.remove_staff_functions),

    path('update_staff/<int:id>', views.update_staff),
    path('change_staff/<int:id>', views.change_staff),

    ################################################# VEHICLE #################################################

    path('new_model/', views.new_model),
    path('add_new_model/', views.add_new_model),

    path('remove_vehicle/', views.remove_vehicle),
    path('remove_vehicle_functions/<int:id>', views.remove_vehicle_functions),

    path('update_vehicle/<int:id>', views.update_vehicle),
    path('change_vehicle/<int:id>', views.change_vehicle),

    ################################################# SPARE #################################################

    path('add_part/', views.add_part),
    path('add_new_part/', views.add_new_part),

    path('remove_price/', views.remove_price),
    path('remove_price_functions/<int:id>', views.remove_price_functions),

    path('update_spare/<int:id>', views.update_spare),
    path('change_spare/<int:id>', views.change_spare),

    ################################################# SERVICE #################################################

    path('new_service/', views.new_service),
    path('add_new_service/', views.add_new_service),

    path('remove_service/', views.remove_service),
    path('remove_service_functions/<int:id>', views.remove_service_functions),

    path('update_service/<int:id>', views.update_service),
    path('change_service/<int:id>', views.change_service),

    ################################################# REVIEW #################################################

    path('give_review/', views.give_review),
    path('new_give_review/', views.new_give_review),

    ################################################# COMPLAINT #################################################

    path('give_complaint/', views.give_complaint),
    path('new_give_complaint/', views.new_give_complaint),

    ################################################# REGISTER #################################################

    path('register/', views.register),
    path('new_register/', views.new_register),

    ################################################# Login #################################################

    path('login/', views.login),
    path('log/', views.log),

    ################################################# Home #################################################

    path('admin_home/', views.admin_home),
    path('customer_home/', views.customer_home),
    path('sales_home/', views.sales_home),
    path('service_home/', views.service_home),

    path('view_model_page/', views.view_model_page),
    path('book_vehicle/<int:id>', views.book_vehicle)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
