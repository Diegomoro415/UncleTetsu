from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def menu_page(request):
    return render(request, 'menu.html')


def reservation_page(request):
    return render(request, 'reservation.html')


def contact_page(request):
    return render(request, 'contact.html')
