from django.db import models, connection

NULLABLE = {
    'blank': True,
    'null': True,
}


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    cost = models.IntegerField(verbose_name='Цена')
    first_date = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    last_date = models.DateTimeField(verbose_name='Дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.cost}.\n{self.description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('category',)
