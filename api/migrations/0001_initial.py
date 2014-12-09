# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuckFinderUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(unique=True, max_length=250)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)])),
                ('sex', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('prefered_sex', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('prefered_age_min', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)])),
                ('prefered_age_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)])),
                ('last_location', django.contrib.gis.db.models.fields.PointField(srid=4326, max_length=40, null=True)),
                ('prefered_radius', models.IntegerField(default=5, help_text=b'in kilometers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
