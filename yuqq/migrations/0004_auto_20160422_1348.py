# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuqq', '0003_news_tips'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tips',
            old_name='answer',
            new_name='content',
        ),
    ]
