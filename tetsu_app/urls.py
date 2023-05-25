from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('menu/', views.menu_page, name='menu'),
    path('reservation/', views.reservation_page, name='reservation'),
    path('contact/', views.contact_page, name='contact'),
]
