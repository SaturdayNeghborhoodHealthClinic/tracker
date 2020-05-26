# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-26 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dose', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('total_inventory', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrugCategory',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MeasuringUnit',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='drug',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.DrugCategory'),
        ),
        migrations.AddField(
            model_name='drug',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.MeasuringUnit'),
        ),
    ]
