# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('brief_intro', models.CharField(max_length=255, null=True)),
                ('raise_method', models.CharField(max_length=255, null=True)),
                ('use_method', models.CharField(max_length=255, null=True)),
                ('remarks', models.CharField(max_length=255, null=True)),
                ('pic1', models.CharField(max_length=40, null=True)),
                ('pic2', models.CharField(max_length=40, null=True)),
                ('type', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('price_low', models.CharField(max_length=8, null=True)),
                ('price_high', models.CharField(max_length=8, null=True)),
                ('slogan', models.CharField(max_length=50, null=True)),
                ('catalogue', models.CharField(max_length=10, null=True)),
                ('inventory', models.CharField(max_length=5, null=True)),
                ('time_to_market', models.DateField(null=True)),
                ('pic1', models.CharField(max_length=40, null=True)),
                ('pic2', models.CharField(max_length=40, null=True)),
                ('pic3', models.CharField(max_length=40, null=True)),
                ('pic4', models.CharField(max_length=40, null=True)),
                ('pic5', models.CharField(max_length=40, null=True)),
                ('related1', models.CharField(max_length=30, null=True)),
                ('related2', models.CharField(max_length=30, null=True)),
                ('related3', models.CharField(max_length=30, null=True)),
                ('related4', models.CharField(max_length=30, null=True)),
                ('popularity', models.CharField(max_length=50, null=True)),
                ('remarks', models.CharField(max_length=50, null=True)),
                ('introduction', models.OneToOneField(null=True, to='yuqq.Introduction')),
            ],
        ),
    ]
