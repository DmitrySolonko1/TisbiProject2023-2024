from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    date_publishing = models.DateField(auto_now=False, auto_now_add=True)
    author = models.CharField(max_length=255, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
