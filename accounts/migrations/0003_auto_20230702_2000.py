# Generated by Django 3.2.15 on 2023-07-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_project_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='miscellaneous',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='rights_total',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='story_rights',
            field=models.IntegerField(blank=True),
        ),
    ]
