from django.db import models
from ckeditor.fields import RichTextField


class Ology(models.Model):
    title_glub = models.CharField(max_length=225, verbose_name='Заголовок главный', blank=True, null=True)
    description_glub = RichTextField(max_length=225, verbose_name='Описание главный', blank=True, null=True)
    title = models.CharField(max_length=225, verbose_name='Общество', blank=True, null=True)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    number = models.CharField(verbose_name='Номер', max_length=225, blank=True, null=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    link = models.CharField(verbose_name='Сыллка', max_length=225, blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наука'
        verbose_name_plural = 'Науки'

class OlogyObject(models.Model):
    ology = models.ForeignKey(Ology,verbose_name='Обект образавания', on_delete=models.CASCADE)
    title = models.CharField(max_length=225, verbose_name='Заголовок', blank=True, null=True)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    link = models.URLField(verbose_name='Сыллка', blank=True, null=True)
