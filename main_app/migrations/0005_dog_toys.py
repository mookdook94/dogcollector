# Generated by Django 4.2.3 on 2023-08-01 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_toy_delete_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
