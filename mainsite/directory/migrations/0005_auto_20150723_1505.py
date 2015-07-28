# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_auto_20150723_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodmap',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='foodmap',
            name='base_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='foodmap',
            name='base_unit',
            field=models.CharField(max_length=10, null=True, choices=[('g', 'g'), ('kg', 'kg'), ('mg', 'mg'), ('fl oz', 'fl oz'), ('oz', 'oz'), ('L', 'L'), ('mL', 'mL')]),
        ),
        migrations.AlterField(
            model_name='foodmap',
            name='unit',
            field=models.CharField(max_length=10, null=True, choices=[('g', 'g'), ('kg', 'kg'), ('mg', 'mg'), ('fl oz', 'fl oz'), ('oz', 'oz'), ('L', 'L'), ('mL', 'mL')]),
        ),
    ]
