from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(ScientificJournal)
class ScientificJournalsTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ScientificJournalObject)
class ScientificJournalObjectTranslationOptions(TranslationOptions):
    fields = ('description',)
@register(Detail)
class DetailTranslationOptions(TranslationOptions):
    fields = ('detail',)

@register(ScientificJournalWork)
class ScientificJournalWorkTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
