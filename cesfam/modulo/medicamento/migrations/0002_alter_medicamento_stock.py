# Generated by Django 4.0.5 on 2022-07-09 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='stock',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
