# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20210516_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='answer',
            field=models.CharField(max_length=200),
        ),
    ]
