# Generated by Django 4.2.7 on 2023-11-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0003_bio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='full_text',
            field=models.TextField(max_length=7500, verbose_name='Текст'),
        ),
    ]
