from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(LeadershipType)
class LeadershipTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(LeadershipObject)
class LeadershipObjectTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Leadership)
class LeadershipTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'name',
        'position',
        'responsibilities',
        'contact',
    )
