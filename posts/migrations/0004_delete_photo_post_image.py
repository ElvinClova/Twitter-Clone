# Generated by Django 4.0.3 on 2022-03-21 23:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
    ]
