# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_auto_20150714_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='components',
            field=models.ManyToManyField(related_name='component+', through='directory.FoodMap', to='directory.Food'),
        ),
    ]
