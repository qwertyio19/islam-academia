from django.db import models
from ckeditor.fields import RichTextField

class ScientificJournal(models.Model):
    title = models.CharField(max_length=225, verbose_name='Тип информации', blank=True, null=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Detail(models.Model):
    dels = models.ForeignKey(ScientificJournal, on_delete=models.CASCADE, verbose_name='Детально')
    detail = RichTextField(verbose_name='детально', blank=True, null=True)
    img = models.ImageField(upload_to='studentns', blank=True, null=True)

    class Meta:
        verbose_name = 'Детально'
        verbose_name_plural = 'Детально'


class ScientificJournalObjectImage(models.Model):
    cloj = models.ForeignKey(ScientificJournal, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображения', upload_to='logo/', blank=True, null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Избражения'


class ScientificJournalObject(models.Model):
    student = models.ForeignKey(ScientificJournal, on_delete=models.CASCADE, verbose_name='Студент')
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    images = models.ManyToManyField(ScientificJournalObjectImage, related_name='image_deteil', blank=True)

    class Meta:
        verbose_name = 'Обекты Студента'
        verbose_name_plural = 'Объекты Студентов'


class ScientificJournalWork(models.Model):
    student = models.ForeignKey(ScientificJournal, on_delete=models.CASCADE, related_name='works', verbose_name='Студент')
    name = models.CharField(max_length=255, verbose_name='Имя сотрудника')
    description = models.TextField(verbose_name='Описание сотрудника')
    img = models.ImageField(upload_to='work/', verbose_name='Изображение сотрудника')
    detail = models.ManyToManyField(Detail, related_name='work_details', blank=True)

    class Meta:
        verbose_name = 'Работа студента'
        verbose_name_plural = 'Работы студентов'
