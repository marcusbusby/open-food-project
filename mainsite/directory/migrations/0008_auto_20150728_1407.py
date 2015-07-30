# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.template.defaultfilters import slugify

def make_slug(apps, schema_editor):
	Food = apps.get_model("directory", "Food")
	for food in Food.objects.all():
		food.slug = slugify(food.name)
		food.save()

class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0007_food_slug'),
    ]

    operations = [
    	migrations.RunPython(make_slug),
    ]
