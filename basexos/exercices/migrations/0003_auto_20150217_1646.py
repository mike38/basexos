# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('exercices', '0002_auto_20150216_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercice',
            name='motclef',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags', through='taggit.TaggedItem', to='taggit.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test_files',
            name='fichier',
            field=models.FileField(upload_to='/home/mike/django/basexos/basexos/basexos/media/'),
            preserve_default=True,
        ),
    ]
