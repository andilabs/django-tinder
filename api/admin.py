from mapwidgets.widgets import GoogleMapPointFieldWidget

from django.contrib import admin
from django.contrib.gis.db import models

from api.models import DjTinderUser


@admin.register(DjTinderUser)
class DjTinderUserAdmin(admin.ModelAdmin):
    list_display = [
        'nickname',
        'age',
        'sex',
        'preferred_radius',
        'age',
        'preferred_age_min',
        'preferred_age_max'
    ]
    list_filter = [
        'preferred_radius',
        'sex',
        'age',
        'preferred_age_min',
        'preferred_age_max'
    ]
    search_fields = ['nickname', 'body']
    ordering = ['preferred_radius', 'sex']
    show_facets = admin.ShowFacets.ALWAYS
    formfield_overrides = {
        models.PointField: {"widget": GoogleMapPointFieldWidget}
    }
