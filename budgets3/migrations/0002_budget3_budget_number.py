# Generated by Django 3.2.15 on 2024-02-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget3',
            name='budget_number',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
