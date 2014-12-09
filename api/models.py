#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.validators import MinValueValidator, MaxValueValidator


SEX_CHOICES = (
    ('F', 'Female',),
    ('M', 'Male',),
)

class FuckFinderUser(models.Model):
    nickname = models.CharField(max_length=250, unique=True)

    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(130)])

    # sex = models.BooleanField(choices=SEX, db_index=True, default=False)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    # prefered_sex = models.BooleanField(choices=SEX, default=True, db_index=True)
    prefered_sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    prefered_age_min = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(130)])
    prefered_age_max = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(130)])

    # latitude = models.DecimalField(max_digits=8, decimal_places=5)
    # longitude = models.DecimalField(max_digits=8, decimal_places=5)

    last_location = models.PointField(max_length=40, null=True)

    prefered_radius = models.IntegerField(default=5, help_text="in kilometers")

    objects = models.GeoManager()

    # def save(self, *args, **kwargs):
    #     self.mpoint = Point(float(self.longitude), float(self.latitude))
    #     super(FuckFinderUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.nickname