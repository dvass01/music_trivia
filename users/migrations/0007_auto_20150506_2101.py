# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150501_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.DecimalField(max_digits=12, decimal_places=2, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, default=None),
            preserve_default=False,
        ),
    ]
