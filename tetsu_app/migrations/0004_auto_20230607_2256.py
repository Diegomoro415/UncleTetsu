# Generated by Django 3.2.19 on 2023-06-07 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tetsu_app', '0003_auto_20230603_1954'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='request_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='guest_count',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='seats',
        ),
        migrations.AddField(
            model_name='reservation',
            name='num_people',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
