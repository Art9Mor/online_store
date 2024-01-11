from django.conf import settings
from django.db import models, connection
from django.db.models.signals import post_save
from django.dispatch import receiver

NULLABLE = {
    'blank': True,
    'null': True,
}


class Category(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name',)

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Product(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    cost = models.IntegerField(verbose_name='Цена')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='user', **NULLABLE)
    first_date = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    last_date = models.DateTimeField(verbose_name='Дата изменения', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='В наличии', **NULLABLE)
    can_be_ordered = models.BooleanField(default=True, verbose_name='Можно заказать', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='опубликован', **NULLABLE)

    def __str__(self):
        return f'{self.name} | {self.category} | {self.cost} руб.'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('category',)


class Review(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(unique=True, max_length=100, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='Содержимое')
    photo = models.ImageField(upload_to='review/', verbose_name='Первью', **NULLABLE)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'Отзыв {self.title}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(verbose_name='Номер версии')
    name = models.CharField(max_length=100, verbose_name='Название версии')
    sign = models.BooleanField(default=False, verbose_name='Текущая версия', **NULLABLE)

    def __str__(self):
        return f'Продукт {self.product} версии {self.number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


@receiver(post_save, sender=Version)
def set_current_version(sender, instance, **kwargs):
    if instance.current_version:
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(current_version=False)
