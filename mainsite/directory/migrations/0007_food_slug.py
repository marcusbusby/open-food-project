# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0006_auto_20150728_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
