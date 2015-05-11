# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20150511_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='win_percentage',
            field=models.CharField(max_length=254, default=0),
        ),
    ]
