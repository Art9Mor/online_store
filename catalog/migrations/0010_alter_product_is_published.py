# Generated by Django 4.2.7 on 2024-01-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_product_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='опубликован'),
        ),
    ]
