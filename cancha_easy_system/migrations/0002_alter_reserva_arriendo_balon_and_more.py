# Generated by Django 5.0.6 on 2024-07-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancha_easy_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='arriendo_balon',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='luz_artificial',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
