# Generated by Django 4.2.7 on 2023-12-02 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book2_delete_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book2',
            name='date',
        ),
    ]
