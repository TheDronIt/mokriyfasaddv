# Generated by Django 4.1.3 on 2023-01-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_certificate_visibility_alter_portfolio_wasted_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Название вакансии')),
                ('Description', models.TextField(blank=True, verbose_name='Описание')),
                ('Salary', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Вакансии',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
