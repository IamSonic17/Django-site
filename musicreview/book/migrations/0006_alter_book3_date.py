# Generated by Django 4.2.7 on 2023-12-03 07:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book3_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book3',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
