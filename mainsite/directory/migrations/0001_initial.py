# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
          migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('parent', models.ForeignKey(blank=True, to='directory.Company', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL))
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('company', models.ForeignKey(blank=True, to='directory.Company', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL))

            ],
        ),
        migrations.CreateModel(
            name='FoodMap',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(choices=[('g', 'g'), ('kg', 'kg'), ('fl oz', 'fl oz'), ('oz', 'oz')], max_length=10)),
                ('base_amount', models.IntegerField()),
                ('base_unit', models.CharField(choices=[('g', 'g'), ('kg', 'kg'), ('fl oz', 'fl oz'), ('oz', 'oz')], max_length=10)),
                ('citation', models.CharField(max_length=200)),
                ('component', models.ForeignKey(related_name='component', to='directory.Food')),
                ('target', models.ForeignKey(related_name='target', to='directory.Food')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL))
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='components',
            field=models.ManyToManyField(related_name='component+', blank=True, to='directory.Food', through='directory.FoodMap', null=True),
        ),
    ]
