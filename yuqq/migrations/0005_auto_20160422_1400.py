# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuqq', '0004_auto_20160422_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tips',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
