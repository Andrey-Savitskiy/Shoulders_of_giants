from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Scientist(models.Model):
    name = models.CharField(max_length=500, verbose_name='ФИО')
    short_description = models.CharField(max_length=500, verbose_name='Краткое описание')
    full_description = models.CharField(max_length=500, verbose_name='Полное описание')
    photo = models.ImageField(upload_to='photos/scientists', verbose_name='Фото')
    life_years = models.CharField(max_length=50, verbose_name='Годы жизни')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ученый'
        verbose_name_plural = 'Ученые'
        ordering = ['name']


class Invention(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    short_description = models.CharField(max_length=500, verbose_name='Краткое описание')
    full_description = models.CharField(max_length=500, verbose_name='Полное описание')
    photo = models.ImageField(upload_to='photos/scientists', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изобретение'
        verbose_name_plural = 'Изобретения'
        ordering = ['title']


class Year(models.Model):
    date = models.IntegerField(verbose_name='Год',
                               validators=[MinValueValidator(1930), MaxValueValidator(datetime.date.today().year)])

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Годы'
        ordering = ['-date']
