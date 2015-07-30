# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0005_auto_20150723_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='entry_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='companyphoto',
            name='entry_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='food',
            name='entry_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='foodmap',
            name='entry_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='foodphoto',
            name='entry_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='foodmap',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodmap',
            name='base_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodmap',
            name='base_unit',
            field=models.CharField(choices=[('g', 'g'), ('kg', 'kg'), ('mg', 'mg'), ('fl oz', 'fl oz'), ('oz', 'oz'), ('L', 'L'), ('mL', 'mL')], null=True, max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='foodmap',
            name='unit',
            field=models.CharField(choices=[('g', 'g'), ('kg', 'kg'), ('mg', 'mg'), ('fl oz', 'fl oz'), ('oz', 'oz'), ('L', 'L'), ('mL', 'mL')], null=True, max_length=10, blank=True),
        ),
    ]
