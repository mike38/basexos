# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_files',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('fichier', models.FileField(upload_to='Fichiers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='files',
            old_name='format',
            new_name='format_fichier',
        ),
        migrations.RemoveField(
            model_name='files',
            name='type',
        ),
        migrations.AddField(
            model_name='files',
            name='correction',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='files',
            name='fichier',
            field=models.FileField(upload_to='Fichiers'),
            preserve_default=True,
        ),
    ]
