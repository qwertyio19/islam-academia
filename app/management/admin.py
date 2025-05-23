from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from .translation import *
from django.forms import ModelForm

class LeadershipObjectModelForm(ModelForm):
    class Meta: 
        model = Leadership
        fields = '__all__'

class LeadershipObjectInline(admin.TabularInline):
    model = LeadershipObject
    extra = 1


@admin.register(LeadershipType)
class LeadershipTypeAdmin(TranslationAdmin):
    list_display = ('name', 'code')
    prepopulated_fields = {'code': ('name',)}

@admin.register(Leadership)
class LeadershipAdmin(TranslationAdmin):
    list_display = ('title', 'type', 'name', 'position', 'email', 'phone', 'date_publication')
    list_filter = ('type',)
    search_fields = ('title', 'name', 'position', 'email', 'phone', 'contact')
    ordering = ('-date_publication',)

    fieldsets = (
        ("Основная информация", {
            'fields': ('type', 'title', 'name', 'position', 'image')
        }),
        ("Контактные данные и файл", {
            'fields': ('email', 'phone', 'contact', 'date_publication')
        }),
        ("Обязанности, Требования, Условия", {
            'fields': ('responsibilities',)
        }),
    )
    inlines = [LeadershipObjectInline]
