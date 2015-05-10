# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150430_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]
