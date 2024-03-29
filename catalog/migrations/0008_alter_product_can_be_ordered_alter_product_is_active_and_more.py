# Generated by Django 4.2.7 on 2024-01-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='can_be_ordered',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Можно заказать'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='В наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='опубликован'),
        ),
        migrations.AlterField(
            model_name='version',
            name='sign',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Текущая версия'),
        ),
    ]
