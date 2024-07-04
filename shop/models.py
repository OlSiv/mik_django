from datetime import datetime 
from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Section(models.Model):
    title = models.CharField(
        max_length=70,
        help_text='Тут нужно ввести название раздела',
        unique=True,
        verbose_name='Название раздела'
    )

    class Meta:
        ordering = ['id'] # по какому полю сортировка
        verbose_name = 'Раздел'
        # - определяет название в админке БД 
        verbose_name_plural = 'Разделы'
        # - название для множественного числа 

    # - вариант отображения объекта по умолчанию - 
    def __str__(self):
        return self.title 

class Product(models.Model):
    section = models.ForeignKey(
        'Section', 
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name='Раздел',
    )
    title = models.CharField(
        max_length=70, 
        verbose_name='Название',
    )
    image = models.ImageField(
        upload_to='images',
        verbose_name='Изображение',
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,   # count digits after dot
        verbose_name='Цена',
    )
    year = models.IntegerField(
        validators=[MinValueValidator(1900), 
                    MaxValueValidator(datetime.date.today().year)],
        verbose_name='Год'
    )
    country = models.CharField(
        max_length=70, 
        verbose_name='Страна',
    )
    director = models.CharField(
        max_length=70, 
        verbose_name='Режисёр',
    )
    play = models.IntegerField(
        validators=[MinValueValidator(1)],
        null = True, 
        blank = True, 
        verbose_name='Продолжительность',
        help_text='В секундах',
    )
    cast = models.TextField(verbose_name='В ролях')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(
        auto_now_add=True, 
        verbose_name='Дата добавления'
    )

    class Meta:
        ordering = ['title', '-year'] 
        # по какому полю сортировка, "-" - по убыванию 
        verbose_name = 'Товар'
        # - определяет название в админке БД 
        verbose_name_plural = 'Товары'
        # - название для множественного числа 

    # - вариант отображения объекта по умолчанию - 
    def __str__(self):
        return '{0} ({1})'.format(self.title, self.section)
    # - название фильма и в скобках раздел 

class Discount(models.Model):
    code = models.CharField(max_length=10, verbose_name='Код купона')
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name='Размер скидки',
        help_text='В процентах'
    )

    class Meta:
        ordering = ['-value'] 
        # по какому полю сортировка, "-" - по убыванию 
        verbose_name = 'Скидка'
        # - определяет название в админке БД 
        verbose_name_plural = 'Скидки'
        # - название для множественного числа 

    # - вариант отображения объекта по умолчанию - 
    def __str__(self):
        return self.code + ' (' + str(self.value) + '%)'

