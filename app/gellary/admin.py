from django.contrib import admin
from .models import *
from . translation import *


# Register your models here.
class PhotosAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Фотография', {
            'fields': ['photo', 'date'],
        }),
        ('Русская версия', {
        'fields': ['title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky'],
        }),
        ('Английская версия', {
            'fields': ['title_en'],
        })
    )
       


admin.site.register(Photos, PhotosAdmin)