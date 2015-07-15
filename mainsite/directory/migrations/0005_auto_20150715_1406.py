# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_auto_20150714_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='components',
            field=models.ManyToManyField(blank=True, through='directory.FoodMap', null=True, to='directory.Food', related_name='component+'),
        ),
    ]
