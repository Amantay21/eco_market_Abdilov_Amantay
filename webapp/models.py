from django.db import models

class ProdCategory(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=20000, null=False, blank=False, verbose_name='Описание')
    image = models.CharField(max_length=200, null=False, blank=False, verbose_name='Фото')

    def __str__(self):
        return f'{self.id}. {self.title}'


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    image = models.CharField(max_length=200, null=False, blank=False, verbose_name='Фото')
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Цена")
    prod_category = models.ForeignKey('webapp.ProdCategory', on_delete=models.RESTRICT, verbose_name='Категория')

    def __str__(self):
        return f'{self.id}. {self.title}'
