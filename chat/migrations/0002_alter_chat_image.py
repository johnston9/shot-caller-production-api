# Generated by Django 3.2.15 on 2023-08-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
