# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuqq', '0002_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('answer', models.CharField(max_length=255, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('popularit', models.CharField(max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('answer', models.CharField(max_length=255, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('popularit', models.CharField(max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
