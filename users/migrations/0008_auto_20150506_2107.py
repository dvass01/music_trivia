# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150506_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 6, 21, 7, 32, 578401, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 5, 6, 21, 7, 37, 34423, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=12, default=0.0),
        ),
    ]
