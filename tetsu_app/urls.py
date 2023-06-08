from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('menu/', views.menu_page, name='menu'),
    path('reservation/', views.reservation_page, name='reservation'),
    path('contact/', views.contact_page, name='contact'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
]
