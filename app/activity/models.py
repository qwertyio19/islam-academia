from django.db import models
from ckeditor.fields import RichTextField

class Activity(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка', blank=True, null=True
    )
    description = RichTextField(
        verbose_name = 'Описание',
        blank=True, null=True
    )
    date = models.CharField(
        max_length = 155,
        verbose_name = 'Дата', blank=True, null=True
    )
    title_obj = models.CharField(
        max_length=155,
        verbose_name='Заголовка Объекта', blank=True, null=True
    )
    description_obj = RichTextField(
        verbose_name='Описание Объекта', blank=True, null=True
    )
    image = models.ImageField(
        upload_to='activity',
        verbose_name='Фото', blank=True, null=True
    )
    place = models.CharField(
        max_length = 155,
        verbose_name = 'Место', blank=True, null=True
    )
    link = models.CharField(max_length=155, verbose_name='Категория', blank=True, null=True)

    def __str__(self):
        return  self.title

    class Mate:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельности'
