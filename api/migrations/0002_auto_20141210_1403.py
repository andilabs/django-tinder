# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuckfinderuser',
            name='age',
            field=models.IntegerField(db_index=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fuckfinderuser',
            name='prefered_age_max',
            field=models.IntegerField(db_index=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fuckfinderuser',
            name='prefered_age_min',
            field=models.IntegerField(db_index=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fuckfinderuser',
            name='prefered_sex',
            field=models.CharField(db_index=True, max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fuckfinderuser',
            name='sex',
            field=models.CharField(db_index=True, max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')]),
            preserve_default=True,
        ),
    ]
