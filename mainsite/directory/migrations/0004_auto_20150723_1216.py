# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_auto_20150722_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='edit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='edit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='foodmap',
            name='edit',
            field=models.BooleanField(default=False),
        ),
    ]
