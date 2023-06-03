from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages


def home_page(request):
    return render(request, 'home.html')


def menu_page(request):
    return render(request, 'menu.html')


def reservation_page(request):
    return render(request, 'reservation.html')


def contact_page(request):
    return render(request, 'contact.html')
