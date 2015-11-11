# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_remove_movie_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='funny',
        ),
    ]
