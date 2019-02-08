from mapwidgets.widgets import GooglePointFieldWidget

from django.contrib import admin
from django.contrib.gis.db import models

from api.models import DjTinderUser


@admin.register(DjTinderUser)
class DjTinderUserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
