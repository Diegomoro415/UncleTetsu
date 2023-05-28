from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('menu/', views.menu_page, name='menu'),
    path('reservation/', views.reservation_page, name='reservation'),
    path('contact/', views.contact_page, name='contact'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
