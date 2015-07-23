# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_companyphoto_foodphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyphoto',
            name='title',
            field=models.CharField(max_length=50, default='old'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodphoto',
            name='title',
            field=models.CharField(max_length=50, default='old'),
            preserve_default=False,
        ),
    ]
