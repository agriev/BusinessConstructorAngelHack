# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BCBusinessModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=2050)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BCBusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('outcomeOneTime', models.FloatField()),
                ('outcomeMonthly', models.FloatField()),
                ('incomeMonthly', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BCUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=250)),
                ('businessmodels', models.ManyToManyField(to='BCApp.BCBusinessModel')),
                ('businessunits', models.ManyToManyField(to='BCApp.BCBusinessUnit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bcbusinessmodel',
            name='businessunits',
            field=models.ManyToManyField(to='BCApp.BCBusinessUnit'),
            preserve_default=True,
        ),
    ]
