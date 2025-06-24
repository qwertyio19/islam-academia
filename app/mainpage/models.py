from django.db import models
from ckeditor.fields import RichTextField

class Settings(models.Model):
    
    phone_header = models.CharField(max_length=155, verbose_name='Номер телефона в Хедере', blank=True, null=True)
    insta_url = models.URLField(verbose_name='Ссылка на Инстаграм', blank=True, null=True)
    face_book = models.URLField(verbose_name='Ссылка на Фейсбук', blank=True, null=True)
    email_footer = models.CharField(max_length=155, verbose_name='Почта на футоре', blank=True, null=True)
    location = models.CharField(max_length=355, verbose_name='Локация', blank=True, null=True)
    title_banner = models.CharField(max_length=155, verbose_name='Заголовка Баннера', blank=True, null=True)
    description_banner = RichTextField(verbose_name='Описание Баннера', blank=True, null=True)
    image_banner = models.ImageField(upload_to='settings', verbose_name='Фото Баннера', blank=True, null=True)

    title_news = models.CharField(max_length=155, verbose_name='Заголовка Новости', blank=True, null=True)
    title_scientific_degrees = models.CharField(max_length=155, verbose_name='Заголовка научные степени', blank=True, null=True)
    title_additional_professional_education = models.CharField(max_length=155, verbose_name='Заголовка дополнительная профессиональная образования', blank=True, null=True)
    title_courses = models.CharField(max_length=155, verbose_name='Заголовка Курсов', blank=True, null=True)
    title_we_suggest_you_watch_it = models.CharField(max_length=155, verbose_name='Заголовка Предлогаем к просмотру', blank=True, null=True)
    title_journal_of_the_islamic_academy = models.CharField(max_length=155, verbose_name='Заголовка журнал исламской академии', blank=True, null=True)
    title_journals_of_partner_universities = models.CharField(max_length=155, verbose_name='Заголовка журналы партнерских вузов', blank=True, null=True)
    title_gallery = models.CharField(max_length=155, verbose_name='Заголовка Галлерий', blank=True, null=True)
    
    obj_date = models.CharField(max_length=255, verbose_name='Дата Объекта Предлогаем к просмотру', blank=True, null=True)
    title_obj = models.CharField(max_length=155, verbose_name='Заголовка Объекта Предлогаем к просмотру', blank=True, null=True)
    description_obj = RichTextField(verbose_name='Описание Объекта Предлогаем к просмотру', blank=True, null=True)

    image_obj = models.ImageField(upload_to='settings/obj', verbose_name='Фото Объекта Предлогаем к просмотру', blank=True, null=True)
    image_above = models.ImageField(upload_to='logo/', verbose_name='Изображение вверху', blank=True, null=True)
    image_below = models.ImageField(upload_to='logo/', verbose_name='Изображение снизу', blank=True, null=True)

    date_headers = models.CharField(max_length=225, verbose_name='Дата', blank=True, null=True)
    date_muslim = models.CharField(max_length=225, verbose_name='Дата мусульманская', blank=True, null=True)
    
    title_1 = models.CharField(max_length=225, verbose_name='Заголовок первый', blank=True, null=True)
    title_2 = models.CharField(max_length=225, verbose_name='Заголовок второй', blank=True, null=True)
    title_3 = models.CharField(max_length=225, verbose_name='Заголовок третий', blank=True, null=True)
    title_4 = models.CharField(max_length=225, verbose_name='Заголовок чётвёртый', blank=True, null=True)
    title_5 = models.CharField(max_length=225, verbose_name='Заголовок пятый', blank=True, null=True)
    title_6 = models.CharField(max_length=225, verbose_name='Заголовок шестой', blank=True, null=True)
    title_7 = models.CharField(max_length=225, verbose_name='Заголовок седьмой', blank=True, null=True)
    title_8 = models.CharField(max_length=225, verbose_name='Заголовок восьмой', blank=True, null=True)


    class Meta:
        verbose_name = 'Настройки Главной Страницы'
        verbose_name_plural = 'Настройки Главной Страницы'


class SettingsObject(models.Model):
    settings_object = models.ForeignKey(Settings, on_delete=models.CASCADE, verbose_name='Настройки', related_name='settings_objects')
    link = models.URLField(verbose_name='Сыллка в главной', blank=True, null=True)
    text_link = models.CharField(verbose_name='Текст для сыллки', max_length=225, blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', verbose_name='Логотип для сыллки', blank=True, null=True)
    

class NewsMain(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголловок')
    description = RichTextField(verbose_name='Заголловок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовки новостей'
        verbose_name_plural = 'Заголовки новостей'
    

class NewsCard(models.Model):
    page = models.ForeignKey(NewsMain, on_delete=models.CASCADE, related_name='cards')
    date = models.CharField(max_length=155,verbose_name='Заголловок')
    title = models.CharField(max_length=255)
    text = RichTextField(verbose_name='Заголловок')
    image = models.ImageField(upload_to='cards/', verbose_name='Заголловок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта новостей'
        verbose_name_plural = 'Карты новостей'

class Magazine(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголловок')
    description = RichTextField(verbose_name='Заголловок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовки Журналов'
        verbose_name_plural = 'Заголовки Журналов'

class MagazineCard(models.Model):
    page = models.ForeignKey(Magazine, on_delete=models.CASCADE, related_name='cards')
    date = models.CharField(max_length=155, verbose_name='Заголловок')
    title = models.CharField(max_length=255, verbose_name='Заголловок')
    text = RichTextField(verbose_name='Заголловок')
    image = models.ImageField(upload_to='missions/', verbose_name='Заголловок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Журналов'
        verbose_name_plural = 'Журналов'