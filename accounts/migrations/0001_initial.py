# Generated by Django 3.2.15 on 2023-07-02 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
                ('url', models.CharField(blank=True, max_length=25)),
                ('stripe_id', models.CharField(blank=True, max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=25)),
                ('series', models.CharField(blank=True, max_length=25)),
                ('prodco', models.CharField(blank=True, max_length=25)),
                ('format', models.CharField(blank=True, max_length=25)),
                ('location', models.CharField(blank=True, max_length=25)),
                ('dated', models.CharField(blank=True, max_length=25)),
                ('research', models.IntegerField(blank=True)),
                ('prep', models.IntegerField(blank=True)),
                ('shoot', models.IntegerField(blank=True)),
                ('wrap', models.IntegerField(blank=True)),
                ('post', models.IntegerField(blank=True)),
                ('length_total', models.IntegerField(blank=True)),
                ('story_rights', models.IntegerField(blank=True)),
                ('miscellaneous', models.IntegerField(blank=True)),
                ('rights_total', models.IntegerField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.project')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
