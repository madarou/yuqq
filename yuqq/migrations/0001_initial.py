# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=255, null=True)),
                ('answer', models.CharField(max_length=255, null=True)),
                ('ask_time', models.DateTimeField(null=True)),
                ('answer_time', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('price', models.CharField(max_length=8, null=True)),
                ('slogan', models.CharField(max_length=50, null=True)),
                ('pic', models.CharField(max_length=40, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('contact', models.CharField(max_length=30, null=True)),
                ('content', models.CharField(max_length=255, null=True)),
                ('time', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=30, null=True)),
                ('product_num', models.CharField(max_length=5, null=True)),
                ('product_price', models.CharField(max_length=8, null=True)),
                ('total_cost', models.CharField(max_length=10, null=True)),
                ('user_remark', models.CharField(max_length=80, null=True)),
                ('send_home', models.CharField(max_length=3, null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('fetch_date', models.CharField(max_length=20, null=True)),
                ('contact', models.CharField(max_length=30, null=True)),
                ('send_date', models.CharField(max_length=20, null=True)),
                ('send_address', models.CharField(max_length=50, null=True)),
                ('order_date', models.DateTimeField(null=True)),
                ('actual_cost', models.CharField(max_length=10, null=True)),
                ('yqq_remark', models.CharField(max_length=80, null=True)),
            ],
            options={
                'abstract': False,
            },
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
                ('kind', models.CharField(max_length=20, null=True)),
                ('show', models.CharField(max_length=3, null=True)),
                ('introduction', models.OneToOneField(null=True, to='yuqq.Introduction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10, null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('service_date', models.CharField(max_length=20, null=True)),
                ('contact', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('user_remark', models.CharField(max_length=80, null=True)),
                ('yqq_remark', models.CharField(max_length=80, null=True)),
                ('order_date', models.DateTimeField(null=True)),
                ('actual_cost', models.CharField(max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
