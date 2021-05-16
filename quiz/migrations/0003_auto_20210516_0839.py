# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='answers',
        ),
    ]
