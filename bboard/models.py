from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Bb(models.Model):
    """
    Объявление
    """
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

    def title_and_price(self):
        if self.price:
            return '%s (%.2f)' % (self.title, self.price)
        else:
            return self.title


class Rubric(models.Model):
    """
    Категория для объявлений
    """
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def get_absolute_url(self):
        return '/%s/' % self.pk

class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Qqq(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=20000, default='Null',verbose_name='Описание')