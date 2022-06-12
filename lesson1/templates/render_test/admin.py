from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.SampleModel)
class MarathonsAdmin(admin.ModelAdmin):
    pass
