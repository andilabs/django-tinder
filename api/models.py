#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


SEX_CHOICES = (
    ('F', 'Female',),
    ('M', 'Male',),
)


def hetero_desires(sex):
    return 'M' if sex == 'F' else 'F'


class FuckFinderUser(models.Model):
    nickname = models.CharField(max_length=250, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(130)], db_index=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, db_index=True)
    prefered_sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    prefered_age_min = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(130)])
    prefered_age_max = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(130)])
    last_location = models.PointField(max_length=40, null=True)
    prefered_radius = models.IntegerField(default=5, help_text="in kilometers")
    objects = models.GeoManager()

    def __str__(self):
        return self.nickname

    def hetero_desires(self):
        return hetero_desires(self.sex)
