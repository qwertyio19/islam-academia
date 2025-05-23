from modeltranslation.translator import register, TranslationOptions, translator
from app.mainpage.models import Settings, NewsMain, NewsCard, Magazine, MagazineCard, SettingsObject

@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = (
        'location', 'title_banner', 'description_banner', 'title_news', 'title_scientific_degrees',
        'date_headers', 'title_additional_professional_education', 'title_courses', 'title_we_suggest_you_watch_it',
        'title_journal_of_the_islamic_academy', 'title_journals_of_partner_universities', 'title_gallery',
        'obj_date', 'title_obj', 'description_obj', 'title_1', 'title_2', 'title_3', 'title_4',
        'title_5', 'title_6', 'title_7', 'title_8',
    )

@register(SettingsObject)
class SettingsObjectTranslationOptions(TranslationOptions):
    fields = [
        'text_link',
    ]

@register(NewsMain)
class NewsMainTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(NewsCard)
class NewsCardTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Magazine)
class MagazineTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(MagazineCard)
class MagazineCardTranslationOptions(TranslationOptions):
    fields = ('title', 'text')