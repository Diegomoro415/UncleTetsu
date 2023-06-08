from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ReservationForm
from django.contrib import messages


def home_page(request):
    return render(request, 'home.html')


def menu_page(request):
    return render(request, 'menu.html')


def reservation_page(request):
    return render(request, 'reservation.html')


def make_reservation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.user = request.user
                # Verifique a disponibilidade de mesa no
                # horário e data desejados e atualize o status
                # Aqui você pode adicionar a lógica para
                # verificar a disponibilidade de mesa
                reservation.save()
                return redirect('reservation_success')
        else:
            form = ReservationForm()
        return render(request, 'reservation.html', {'form': form})
    else:
        return redirect('login')


def contact_page(request):
    return render(request, 'contact.html')
