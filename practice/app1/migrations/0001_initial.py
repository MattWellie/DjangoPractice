# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labnum', models.TextField(unique=True)),
                ('firstname', models.TextField()),
                ('surname', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientVariant',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('patient', models.ForeignKey(to='app1.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('genomic_pos', models.IntegerField()),
                ('hgvs', models.TextField()),
                ('occurrences', models.ManyToManyField(to='app1.Patient', through='app1.PatientVariant')),
            ],
        ),
        migrations.AddField(
            model_name='patientvariant',
            name='variant',
            field=models.ForeignKey(to='app1.Variant'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='app1.Question'),
        ),
    ]
