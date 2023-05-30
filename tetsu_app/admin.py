from django.contrib import admin
from .models import (
    FoodMenu, DrinkMenu, Post, Comment, Table,
    Reserva, User, Contato
)


@admin.register(FoodMenu, DrinkMenu, Post, Comment,
                Table, Reserva, User, Contato)
class MyModelAdmin(admin.ModelAdmin):
    pass
