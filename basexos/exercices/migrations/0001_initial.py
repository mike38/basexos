# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=255)),
                ('classe', models.CharField(max_length=20)),
                ('matiere', models.CharField(max_length=255)),
                ('chapitre', models.CharField(max_length=255)),
                ('origine', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fichier', models.FileField(upload_to=b'Fichiers')),
                ('format', models.CharField(max_length=255)),
                ('date_ajout', models.DateField(auto_now_add=True)),
                ('version', models.PositiveSmallIntegerField()),
                ('type', models.CharField(max_length=255)),
                ('id_ex', models.ForeignKey(to='exercices.Exercice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
