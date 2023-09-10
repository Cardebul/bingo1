# Generated by Django 3.2.16 on 2023-08-07 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bingo', '0003_mainmod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmod',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mod', to=settings.AUTH_USER_MODEL),
        ),
    ]
