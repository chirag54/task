# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20210516_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]
