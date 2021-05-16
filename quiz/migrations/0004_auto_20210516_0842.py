# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20210516_0839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='answers',
            new_name='answer',
        ),
    ]
