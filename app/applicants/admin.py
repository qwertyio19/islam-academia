from django.contrib import admin
from .models import *
from . translation import *
from modeltranslation.admin import TranslationAdmin

class AcademicAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английская версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабская версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкая версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
        ('Global', {
            'fields': ['number', 'email'],
        }),
    )
admin.site.register(Academic,AcademicAdmin)
