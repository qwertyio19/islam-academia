from modeltranslation.translator import register, TranslationOptions
from app.AboutAcademy.models import *

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ("page_key", 'title_main', 'title2', 'title_page', 'description',)

@register(AboutObjectPdf)
class AboutObjectPdfTranslationOptions(TranslationOptions):
    fields = ('title', 'title_pdf',)

@register(AboutObject)
class AboutObjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)