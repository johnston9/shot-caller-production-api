# Generated by Django 3.2.15 on 2022-08-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/images/default_profile_iq2tpu', upload_to='images/'),
        ),
    ]
