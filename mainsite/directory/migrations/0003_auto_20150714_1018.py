# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMap',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='company',
            field=models.ForeignKey(to='directory.Company', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='parent',
            field=models.ForeignKey(to='directory.Company', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foodmap',
            name='component',
            field=models.ForeignKey(related_name='component', to='directory.Food'),
        ),
        migrations.AddField(
            model_name='foodmap',
            name='target',
            field=models.ForeignKey(related_name='target', to='directory.Food'),
        ),
        migrations.AddField(
            model_name='food',
            name='components',
            field=models.ManyToManyField(to='directory.Food', through='directory.FoodMap'),
        ),
    ]
