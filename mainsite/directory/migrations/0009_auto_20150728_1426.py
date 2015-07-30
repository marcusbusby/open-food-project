# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0008_auto_20150728_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
