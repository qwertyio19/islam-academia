from django.contrib import admin
from app.AboutAcademy.models import *
from app.AboutAcademy.translation import *
from modeltranslation.admin import TranslationAdmin

class AboutImageInline(admin.TabularInline):
    model = AboutImage
    extra = 1

class AboutObjectIPdfInline(admin.TabularInline):
    model = AboutObjectPdf
    extra = 1

class AboutObjectInsline(admin.TabularInline):
        model = AboutObject
        extra = 1

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    inlines = [AboutImageInline, AboutObjectIPdfInline, AboutObjectInsline,]

    list_display = ('id', 'page_key', 'title_page', 'title_main')
    search_fields = ('title_page', 'page_key')
    fieldsets = (
        ("Ключ", {
            'fields': ('page_key',)
        }),
        ("Русская версия", {
            'fields': ('title_main_ru', 'title2_ru', 'title_page_ru', 'description_ru',)
        }),
        ("Кыргызская версия", {
            'fields': ('title_main_ky', 'title2_ky', 'title_page_ky', 'description_ky',)
        }),
        ("Английская версия", {
            'fields': ('title_main_en', 'title2_en', 'title_page_en', 'description_en',)
        }),
        ("Туркская версия", {
            'fields': ('title_main_tr', 'title2_tr', 'title_page_tr', 'description_tr',)
        }),
        ("Арабская версия", {
            'fields': ('title_main_ar', 'title2_ar', 'title_page_ar', 'description_ar', )
        }),
        ("Global", {
            'fields': ('links_carta', 'number', 'adres', 'rab')
        }),
    )
