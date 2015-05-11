# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_auto_20150510_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice_1',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice_2',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice_3',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice_4',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=254),
        ),
    ]
