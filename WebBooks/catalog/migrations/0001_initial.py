# Generated by Django 4.2.5 on 2023-09-29 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя автора', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Введите фамилию автора', max_length=100, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату рождения', null=True, verbose_name='Дата рождения')),
                ('date_of_death', models.DateField(blank=True, help_text='Введите дату смери', null=True, verbose_name='Дата смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=200, verbose_name='Название кнгиги')),
                ('summary', models.TextField(help_text='Введите краткое описание книги', max_length=500, verbose_name='Описание книги')),
                ('isbn', models.CharField(help_text='Введите ISBN книги. \n                                                        Должно быть 13 символов', max_length=13, verbose_name='ISBN книги')),
                ('author', models.ManyToManyField(help_text='Выберите автора книги', to='catalog.author', verbose_name='Автор книги')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр', max_length=120, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=20, verbose_name='Язык книги')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите статус экземпляра книги', max_length=20, verbose_name='Статус экземпляра книги')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Введите инвентарный номер', max_length=20, null=True, verbose_name='Инвентарный номер')),
                ('imprint', models.CharField(help_text='Введите издательство и год выпуска', max_length=200, verbose_name='Издательство')),
                ('due_back', models.DateField(blank=True, help_text='Введите конец срока статуса', null=True, verbose_name='Дата окончания статуса')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('status', models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Состояние экземпляра')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Выберите жанр', on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Выберите язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Язык книги'),
        ),
    ]
