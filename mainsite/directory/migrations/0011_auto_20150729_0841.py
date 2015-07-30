# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.template.defaultfilters import slugify

def make_slug(apps, schema_editor):
	Company = apps.get_model("directory", "Company")
	for company in Company.objects.all():
		company.slug = slugify(company.name)
		company.save()

class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0010_company_slug'),
    ]

    operations = [
    	migrations.RunPython(make_slug),
    ]
