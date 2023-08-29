# Generated by Django 4.0.5 on 2022-06-29 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carnet_Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('consultorio', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30, verbose_name='Rojo/Amarillo/Verde')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('Run', models.PositiveBigIntegerField(unique=True)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=1, verbose_name='Genero:(M / F)')),
                ('nacimiento', models.DateField()),
                ('especialidad', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=150, unique=True)),
                ('telefono', models.CharField(max_length=13)),
                ('direccion', models.CharField(max_length=70)),
                ('idUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Farmaceuta',
            fields=[
                ('Run', models.PositiveBigIntegerField(unique=True)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=13)),
                ('genero', models.CharField(max_length=1, verbose_name='Genero:(M / F)')),
                ('puesto', models.CharField(max_length=50)),
                ('idUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('Run', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=13)),
                ('cronico', models.CharField(max_length=2)),
                ('tutor', models.CharField(blank=True, max_length=60)),
                ('telefono_tutor', models.CharField(blank=True, max_length=13)),
                ('nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=70)),
                ('genero', models.CharField(max_length=9, verbose_name='Genero:(M / F)')),
                ('correo', models.EmailField(max_length=150, unique=True)),
                ('idCarnet_Paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuario.carnet_paciente')),
            ],
        ),
    ]