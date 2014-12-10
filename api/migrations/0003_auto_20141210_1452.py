# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20141210_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuckfinderuser',
            name='prefered_age_max',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fuckfinderuser',
            name='prefered_age_min',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fuckfinderuser',
            name='prefered_sex',
            field=models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')]),
            preserve_default=True,
        ),
    ]
