# Generated by Django 4.2.16 on 2024-11-08 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='violation',
            name='points',
        ),
    ]