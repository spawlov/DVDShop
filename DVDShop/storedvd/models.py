import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Section(models.Model):
    title = models.CharField(
        max_length=70,
        help_text='Название раздела',
        unique=True,
        verbose_name='Раздел',
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title


class Product(models.Model):
    section = models.ForeignKey(
        Section,
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
        decimal_places=2,
        verbose_name='Цена',
    )
    year = models.SmallIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year)
        ],
        verbose_name='Год',
    )
    country = models.CharField(
        max_length=70,
        verbose_name='Страна',
    )
    director = models.CharField(
        max_length=70,
        verbose_name='Режиссер',
    )
    play = models.SmallIntegerField(
        help_text='В секундах',
        null=True,
        blank=True,
        verbose_name='Продолжительность',
        validators=[MinValueValidator(1)],
    )
    casts = models.TextField(
        verbose_name='В ролях',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата добавления',
    )

    class Meta:
        ordering = ['title', 'year']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title} ({self.section.title})'


class Discount(models.Model):
    code = models.CharField(
        max_length=10,
        verbose_name='Код скидки',
    )
    value = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name='Размер скидки',
        help_text='В процентах',
    )

    class Meta:
        ordering = ['-value']
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.code} ({self.value}%)'


class Order(models.Model):
    need_delivery = models.BooleanField(
        verbose_name='Необходима доставка',
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Скидка',
    )
    name = models.CharField(
        max_length=70,
        verbose_name='Имя',
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
    )
    email = models.EmailField()
    address = models.TextField(
        blank=True,
        verbose_name='Адрес',
    )
    notice = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Примечание',
    )
    date_order = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата заказа',
    )
    date_send = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата отправки',
    )
    STATUSES = [
        ('NEW', 'Новый заказ'),
        ('APR', 'Подтвержден'),
        ('PAY', 'Оплачен'),
        ('CNL', 'Отменён'),
    ]
    status = models.CharField(
        choices=STATUSES,
        max_length=3,
        default='NEW',
        verbose_name='Статус',
    )

    class Meta:
        ordering = ['-date_order']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'ID: {self.pk}'


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Товар',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='Цена',
    )
    count = models.SmallIntegerField(
        validators=[MinValueValidator(1)],
        default=1,
        verbose_name='Количество',
    )

    class Meta:
        verbose_name = 'Строка заказа'
        verbose_name_plural = 'Строки заказа'

    def __str__(self):
        return f'Заказ (ID:{self.order.id}) {self.product.title} {self.count}'
