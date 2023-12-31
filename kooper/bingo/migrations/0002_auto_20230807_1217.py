# Generated by Django 3.2.16 on 2023-08-07 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bingo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BingoModelThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.BooleanField(default=False)),
                ('field2', models.BooleanField(default=False)),
                ('field3', models.BooleanField(default=False)),
                ('field4', models.BooleanField(default=False)),
                ('field5', models.BooleanField(default=False)),
                ('field6', models.BooleanField(default=False)),
                ('field7', models.BooleanField(default=False)),
                ('field8', models.BooleanField(default=False)),
                ('field9', models.BooleanField(default=False)),
                ('old_progress', models.IntegerField(default=0)),
                ('progress', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field10',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field11',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field12',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field13',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field14',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field15',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field16',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field17',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field18',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field19',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field20',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field21',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field22',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field23',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field24',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field25',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field3',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field4',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field5',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field6',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field7',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field8',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='field9',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.CreateModel(
            name='DataModelThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=20)),
                ('field2', models.CharField(max_length=20)),
                ('field3', models.CharField(max_length=20)),
                ('field4', models.CharField(max_length=20)),
                ('field5', models.CharField(max_length=20)),
                ('field6', models.CharField(max_length=20)),
                ('field7', models.CharField(max_length=20)),
                ('field8', models.CharField(max_length=20)),
                ('field9', models.CharField(max_length=20)),
                ('bingo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bingo.bingomodelthree')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='BingoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.BooleanField(default=False)),
                ('field2', models.BooleanField(default=False)),
                ('field3', models.BooleanField(default=False)),
                ('field4', models.BooleanField(default=False)),
                ('field5', models.BooleanField(default=False)),
                ('field6', models.BooleanField(default=False)),
                ('field7', models.BooleanField(default=False)),
                ('field8', models.BooleanField(default=False)),
                ('field9', models.BooleanField(default=False)),
                ('field10', models.BooleanField(default=False)),
                ('field11', models.BooleanField(default=False)),
                ('field12', models.BooleanField(default=False)),
                ('field13', models.BooleanField(default=False)),
                ('field14', models.BooleanField(default=False)),
                ('field15', models.BooleanField(default=False)),
                ('field16', models.BooleanField(default=False)),
                ('field17', models.BooleanField(default=False)),
                ('field18', models.BooleanField(default=False)),
                ('field19', models.BooleanField(default=False)),
                ('field20', models.BooleanField(default=False)),
                ('field21', models.BooleanField(default=False)),
                ('field22', models.BooleanField(default=False)),
                ('field23', models.BooleanField(default=False)),
                ('field24', models.BooleanField(default=False)),
                ('field25', models.BooleanField(default=False)),
                ('old_progress', models.IntegerField(default=0)),
                ('progress', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='datamodel',
            name='bingo',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='bingo.bingomodel'),
            preserve_default=False,
        ),
    ]
