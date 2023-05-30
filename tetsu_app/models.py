from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FoodMenu(models.Model):
    food_name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class DrinkMenu(models.Model):
    drink_name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_date = models.DateField()
    update_date = models.DateField()
    content = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_date = models.DateField()
    approved = models.BooleanField()
    meta = models.CharField(max_length=255)


class Table(models.Model):
    table_name = models.CharField(max_length=255)
    max_seats = models.IntegerField()
    available = models.BooleanField()


class Reserva(models.Model):
    created_date = models.DateField()
    request_date = models.DateField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    guest = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    seats = models.IntegerField()
    guest_count = models.IntegerField()


class User(models.Model):
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date_joined = models.DateTimeField()


class Contato(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
