from statistics import mode
from django.db import models
from django.utils.safestring import mark_safe


class Site(models.Model):

    def __str__(self):
        return 'Найстройки сайта'

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки сайта'


class SiteRules(models.Model):
    site = models.ForeignKey(
        'Site',
        on_delete=models.CASCADE,
    )
    rule = models.TextField(max_length=1000, verbose_name='правило')

    class Meta:
        verbose_name = 'Правила'
        verbose_name_plural = 'Правила'


class SiteContacts(models.Model):
    site = models.ForeignKey(
        'Site',
        on_delete=models.CASCADE,
    )
    number = models.CharField(max_length=200, verbose_name='номер телефона')
    email = models.CharField(max_length=200, verbose_name='email')
    address = models.TextField(max_length=500, verbose_name='адрес')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'




class Rooms(models.Model):
    headname = models.CharField(max_length=100, null=False, verbose_name='название')
    description = models.TextField(max_length=1000, null=False, verbose_name='описание')

    def __str__(self):
        return self.headname

    class Meta:
        verbose_name = 'Комнату'
        verbose_name_plural = 'Комнаты'


class RoomsImages(models.Model):
    rooms = models.ForeignKey(
        'Rooms',
        on_delete=models.CASCADE,
    )
    images = models.FileField(upload_to='images', verbose_name='картинка')

    def image(self):
        return mark_safe(f'<img src="{self.images.url}" width = "200px" />')

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class RoomsCost(models.Model):
    rooms = models.ForeignKey(
        'Rooms',
        on_delete=models.CASCADE,
    )
    cost = models.CharField(max_length=200, verbose_name='пункт')

    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимость'


class RoomsDevices(models.Model):
    rooms = models.ForeignKey(
        'Rooms',
        on_delete=models.CASCADE,
    )
    device = models.CharField(max_length=200, verbose_name='пункт')

    class Meta:
        verbose_name = 'Девайс'
        verbose_name_plural = 'Девайсы'


class RoomsAccessories(models.Model):
    rooms = models.ForeignKey(
        'Rooms',
        on_delete=models.CASCADE,
    )
    accessory = models.CharField(max_length=200, verbose_name='пункт')

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'


class Request(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    number = models.CharField(max_length=100, verbose_name='номер телефона')
    date = models.DateTimeField(auto_now_add=False, verbose_name='дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'заявки'


