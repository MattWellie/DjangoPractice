# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('labnum', models.TextField(unique=True)),
                ('firstname', models.TextField()),
                ('surname', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientVariants',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('patient', models.ForeignKey(to='app1.Patients')),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('genomic_pos', models.IntegerField()),
                ('hgvs', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='patientvariants',
            name='variant',
            field=models.ForeignKey(to='app1.Variants'),
        ),
    ]
