from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
import uuid


STATUS = ((0, "Draft"), (1, "Published"))


class FoodMenu(models.Model):
    food_name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class DrinkMenu(models.Model):
    drink_name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="review_post"
        )
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.table_name


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    num_people = models.IntegerField(default=2, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    request_date = models.DateField(null=True)
    time = models.TimeField(
        default=timezone.now,
        blank=False,
        null=False
    )
    reservation_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.reservation_id)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
