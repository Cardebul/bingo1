# Generated by Django 4.2.3 on 2023-07-09 08:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=18)),
                ('field2', models.CharField(max_length=18)),
                ('field3', models.CharField(max_length=18)),
                ('field4', models.CharField(max_length=18)),
                ('field5', models.CharField(max_length=18)),
                ('field6', models.CharField(max_length=18)),
                ('field7', models.CharField(max_length=18)),
                ('field8', models.CharField(max_length=18)),
                ('field9', models.CharField(max_length=18)),
                ('field10', models.CharField(max_length=18)),
                ('field11', models.CharField(max_length=18)),
                ('field12', models.CharField(max_length=18)),
                ('field13', models.CharField(max_length=18)),
                ('field14', models.CharField(max_length=18)),
                ('field15', models.CharField(max_length=18)),
                ('field16', models.CharField(max_length=18)),
                ('field17', models.CharField(max_length=18)),
                ('field18', models.CharField(max_length=18)),
                ('field19', models.CharField(max_length=18)),
                ('field20', models.CharField(max_length=18)),
                ('field21', models.CharField(max_length=18)),
                ('field22', models.CharField(max_length=18)),
                ('field23', models.CharField(max_length=18)),
                ('field24', models.CharField(max_length=18)),
                ('field25', models.CharField(max_length=18)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
