from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime


class Scientist(models.Model):
    full_name = models.CharField(max_length=128, unique=True, verbose_name='ФИО')
    short_name = models.CharField(max_length=32, verbose_name='Сокращенное ФИО')
    short_description = models.TextField(max_length=512, verbose_name='Краткое описание')
    full_description = models.TextField(max_length=8192, verbose_name='Полное описание')
    photo = models.ImageField(upload_to='img/scientists',
                              verbose_name='Фото')
    # biography = models.TextField(max_length=8192, verbose_name='Биография')
    # life_years = models.CharField(max_length=21, verbose_name='Годы жизни',
    #                               validators=[RegexValidator(r'[0-9]{2}.[0-9]{2}.[0-9]{4}-[0-9]{2}.[0-9]{2}.[0-9]{4}|'
    #                                                          r'[0-9]{2}.[0-9]{2}.[0-9]{4}')])

    start_year = models.ForeignKey('Year', null=True, on_delete=models.PROTECT,
                                   related_name='scientist_start_year', verbose_name='Год рождения')
    end_year = models.ForeignKey('Year', null=True, on_delete=models.PROTECT,
                                 related_name='scientist_end_year', verbose_name='Год смерти',
                                 default=datetime.date.today().year)

    invention = models.ManyToManyField('Invention', blank=True,
                                       related_name='scientist_invention', verbose_name='Изобретение')
    organization = models.ManyToManyField('Organization', blank=True,
                                       related_name='scientist_organization', verbose_name='Организация')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Ученый'
        verbose_name_plural = 'Ученые'
        ordering = ['full_name']


class Organization(models.Model):
    full_name = models.CharField(max_length=128, unique=True, verbose_name='Название')
    short_name = models.CharField(max_length=32, verbose_name='Сокращенное название')
    short_description = models.TextField(max_length=512, verbose_name='Краткое описание')
    full_description = models.TextField(max_length=8192, verbose_name='Полное описание')
    logo = models.ImageField(upload_to='img/organizations',
                             verbose_name='Логотип')
    history = models.TextField(max_length=8192, verbose_name='История')

    start_year = models.ForeignKey('Year', null=True, on_delete=models.PROTECT,
                                   related_name='organization_start_year', verbose_name='Год создания')
    end_year = models.ForeignKey('Year', null=True, on_delete=models.PROTECT,
                                 related_name='organization_end_year', verbose_name='Год расформирования')

    invention = models.ManyToManyField('Invention', blank=True,
                                       related_name='organization_invention', verbose_name='Изобретение')
    scientist = models.ManyToManyField('Scientist', blank=True, through=Scientist.organization.through,
                                       related_name='organization_scientist', verbose_name='Ученый')


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['full_name']


class Invention(models.Model):
    full_title = models.CharField(max_length=128, unique=True, verbose_name='Название')
    short_title = models.CharField(max_length=32, verbose_name='Сокращенное название')
    short_description = models.TextField(max_length=512, verbose_name='Краткое описание')
    full_description = models.TextField(max_length=8192, verbose_name='Полное описание')
    photo = models.ImageField(upload_to='img/inventions',
                              verbose_name='Фото')
    # history = models.TextField(max_length=8192, verbose_name='История')

    year = models.ForeignKey('Year', null=True, on_delete=models.PROTECT, verbose_name='Год создания')

    organization = models.ManyToManyField('Organization', blank=True, through=Organization.invention.through,
                                       related_name='invention_organization', verbose_name='Организация')
    scientist = models.ManyToManyField('Scientist', blank=True, through=Scientist.invention.through,
                                       related_name='invention_scientist', verbose_name='Ученый')

    def __str__(self):
        return self.full_title

    class Meta:
        verbose_name = 'Изобретение'
        verbose_name_plural = 'Изобретения'
        ordering = ['full_title']


class Year(models.Model):
    year = models.IntegerField(verbose_name='Год',  unique=True,
                               validators=[MinValueValidator(1830), MaxValueValidator(datetime.date.today().year)])

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Годы'
        ordering = ['-year']
