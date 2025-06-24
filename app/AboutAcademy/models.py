from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    page_key = models.CharField(
        max_length=100,
        verbose_name="Ключ страницы (пример: about, history, mission)",
        help_text="Используется для группировки и отображения",
        blank=True,
        null=True
    )
    title_main = models.CharField(max_length=200, verbose_name="Главная Заголовка", blank=True, null=True)
    title2 = models.CharField(max_length=155, verbose_name='Под Заголовка', blank=True, null=True)
    title_page = models.CharField(max_length=155, verbose_name='Заголовка Страницы', blank=True, null=True)
    description = RichTextField(verbose_name='Данные о Страницы', blank=True, null=True)
    links_carta = models.CharField(verbose_name='Текст', max_length=225, blank=True, null=True)

    number = models.CharField(max_length=225, verbose_name='Номер', blank=True, null=True)
    adres = models.CharField(max_length=225, verbose_name='Адрес', blank=True, null=True)
    rab = models.CharField(max_length=225, verbose_name='Режим работы', blank=True, null=True)

  



    class Meta:
        verbose_name = 'Об Академий'
        verbose_name_plural = 'Об Академий'

class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='about-academy/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return f"Изображение для {self.about.title_page}"

    class Meta:
        verbose_name = 'Изображение для страницая'
        verbose_name_plural = 'Изображение для страницая'


class AboutObjectPdf(models.Model):
    about_object = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_object_pdf', verbose_name='Обекты Об Академии')
    title = models.CharField(max_length=225, verbose_name='Заголовок', blank=True, null=True)
    title_pdf = models.CharField(max_length=155, verbose_name='Заголовка Файла', blank=True, null=True)
    url_pdf = models.URLField(verbose_name='Ссылка на Файл', blank=True, null=True)
    dowl_url = models.FileField(verbose_name='PDF-Файл', blank=True, null=True)


class AboutObject(models.Model):
    about_object = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_object', verbose_name='Второй обект об академии')
    title = models.CharField(max_length=225, verbose_name='Заголовок', blank=True, null=True)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    images = models.ManyToManyField(AboutImage, related_name='image_deteil', blank=True, null=True)