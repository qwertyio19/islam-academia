from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Ology)
class OlogyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'title_glub', 'description_glub',)

@register(OlogyObject)
class OlogyTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)