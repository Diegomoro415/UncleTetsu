# Generated by Django 3.2.19 on 2023-06-03 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tetsu_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contato',
            new_name='Contact',
        ),
        migrations.RenameModel(
            old_name='Reserva',
            new_name='Reservation',
        ),
    ]