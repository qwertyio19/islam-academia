from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Photos)
class PhotosTranslateOptions(TranslationOptions):
    fields = ('title',)
