# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0005_auto_20150715_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='base_unit',
            field=models.CharField(choices=[('g', 'g'), ('kg', 'kg'), ('fl oz', 'fl oz'), ('oz', 'oz')], max_length=10),
        ),
    ]
