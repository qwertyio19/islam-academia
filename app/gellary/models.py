from django.db import models

# Create your models here.
class Photos(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок сайта',blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    date = models.CharField(max_length=155, verbose_name='Дата', blank=True, null=True)

    def __str__(self):
        return self.date
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
