from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Works(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категории")

    class Meta:
        ordering = ['title']
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})