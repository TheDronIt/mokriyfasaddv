# Generated by Django 4.1.3 on 2023-01-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_portfolioimage_alter_service_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='Visibility',
            field=models.CharField(choices=[('Отображать', 'Отображать'), ('Не отображать', 'Не отображать')], default='Отображать', max_length=50, verbose_name='Отображение'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='Wasted_time',
            field=models.CharField(blank=True, max_length=50, verbose_name='Сроки выполения'),
        ),
    ]