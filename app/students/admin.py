from django.contrib import admin
from .models import *
from .translation import *
from modeltranslation.admin import TranslationAdmin
from django.forms import ModelForm

class ScientificJournalAdminForm(ModelForm):
    class Meta:
        model = ScientificJournal
        fields = '__all__'

class ScientificJournalObjectInline(admin.TabularInline):
    model = ScientificJournalObject
    extra = 1

class ScientificJournalWorkForm(ModelForm):
    class Meta:
        model = ScientificJournalWork
        fields = '__all__'

class ScientificJournalWorkInline(admin.TabularInline):
    model = ScientificJournalWork
    extra = 1

class DetailWorkForm(ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'

class DetailWorkFormInline(admin.TabularInline):
    model = Detail
    extra = 1

class ScientificJournalObjectImageAdminForm(ModelForm):
    class Meta:
        model = ScientificJournalObjectImage
        fields = '__all__'

class ScientificJournalObjectImageInline(admin.TabularInline):
    model = ScientificJournalObjectImage
    extra = 1


class ScientificJournalsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky'],
        }),
        ('Английская версия', {
            'fields': ['title_en'],
        }),
        ('Арабская версия', {
            'fields': ['title_ar'],
        }),
        ('Турецкая версия', {
            'fields': ['title_tr'],
        }),
    )
    inlines = [ScientificJournalObjectInline, ScientificJournalWorkInline, DetailWorkFormInline, ScientificJournalObjectImageInline]
    

admin.site.register(ScientificJournal, ScientificJournalsAdmin)