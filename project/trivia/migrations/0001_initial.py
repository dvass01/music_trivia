# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('genre_name', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('question_text', models.CharField(max_length=100)),
                ('choice_1', models.CharField(max_length=100)),
                ('choice_2', models.CharField(max_length=100)),
                ('choice_3', models.CharField(max_length=100)),
                ('choice_4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('user_answer', models.IntegerField(null=True)),
                ('user_id', models.ForeignKey(to='users.User')),
            ],
        ),
    ]
