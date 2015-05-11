# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20150511_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='games_played',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='win_percentage',
            field=models.CharField(max_length=10, default=0),
        ),
    ]
