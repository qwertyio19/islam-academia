from . models import *
from django.contrib import admin
from . translation import *
from modeltranslation.admin import TranslationAdmin
from django.forms import ModelForm, BaseInlineFormSet


class OlogyAdminForm(ModelForm):
    class Meta:
        model = Ology
        fields = '__all__'


class OlogyObjectInline(admin.TabularInline):  
    model = OlogyObject
    extra = 1 
    verbose_name = "Объект науки"
    verbose_name_plural = "Объекты науки"

class OlogyAdmin(TranslationAdmin):
    form = OlogyAdminForm
    inlines = [OlogyObjectInline]
    
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'title_glub_ru', 'description_glub_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'title_glub_ky', 'description_glub_ky'],
        }),
        ('Английская версия', {
            'fields': ['title_en', 'description_en', 'title_glub_en', 'description_glub_en'],
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




admin.site.register(Ology, OlogyAdmin)

