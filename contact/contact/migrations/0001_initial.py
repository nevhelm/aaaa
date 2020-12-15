# Generated by Django 3.1.1 on 2020-12-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=15, verbose_name='Фамилия')),
                ('big_name', models.CharField(max_length=15, verbose_name='Отчество')),
                ('text_01', models.TextField(max_length=150, verbose_name='Описание')),
                ('birthday', models.DateField(verbose_name='Дата рождение')),
                ('num_ber', models.CharField(max_length=10, verbose_name='Номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Gmail')),
                ('social', models.URLField(verbose_name='Страница в соц сети')),
            ],
            options={
                'verbose_name': 'Имя',
                'verbose_name_plural': 'Имена',
            },
        ),
    ]