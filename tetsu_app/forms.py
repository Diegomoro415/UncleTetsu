from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'phone', 'password1', 'password2')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['num_people', 'date', 'time']
