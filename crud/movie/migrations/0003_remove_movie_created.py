# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20151103_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created',
        ),
    ]
