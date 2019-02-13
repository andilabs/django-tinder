#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


SEX_CHOICES = (
    ('F', 'Female',),
    ('M', 'Male',),
)


def get_opposed_sex(sex):
    return 'M' if sex == 'F' else 'F'


class DjTinderUser(models.Model):
    nickname = models.CharField(max_length=250, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(18),
                                          MaxValueValidator(130)],
                              db_index=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, db_index=True)
    preferred_sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    preferred_age_min = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(130)])
    preferred_age_max = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(130)])
    last_location = models.PointField(max_length=40, null=True)
    preferred_radius = models.IntegerField(default=5,
                                           help_text="in kilometers")

    @property
    def homo(self):
        return self.preferred_sex == self.sex

    def __str__(self):
        return self.nickname

    @property
    def get_opposed_sex(self):
        return get_opposed_sex(self.sex)
