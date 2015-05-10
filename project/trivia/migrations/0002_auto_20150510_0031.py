# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def insert_genres(apps, schema_editor):
    en_names = ['jazz', 'pop', 'rock', 'metal', 'hip-hop', 'folk', 'punk', 'country', 'blues']
    Genre = apps.get_model("trivia", 'Genre')
    for name in en_names:
        this_genre = Genre(genre_name=name)
        this_genre.save()

class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(insert_genres),
    ]
