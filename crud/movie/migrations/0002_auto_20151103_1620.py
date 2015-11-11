# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import datetime




class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default= datetime.datetime.now(), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='funny',
            field=models.BooleanField(default=False),
        ),
    ]
