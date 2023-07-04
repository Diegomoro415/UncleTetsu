from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('menu/', include('menu.urls', namespace='menu')),
    path('reservation/', views.reservation_page, name='reservation'),
    path('contact/', views.contact_page, name='contact'),
]
