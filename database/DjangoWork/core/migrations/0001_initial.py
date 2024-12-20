# Generated by Django 5.1.2 on 2024-10-26 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrafficLaw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('law_code', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violation_code', models.CharField(max_length=10, unique=True)),
                ('penalty', models.DecimalField(decimal_places=2, max_digits=6)),
                ('points', models.IntegerField()),
                ('violation_law', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='violations', to='core.trafficlaw')),
            ],
        ),
    ]
