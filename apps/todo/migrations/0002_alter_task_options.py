# Generated by Django 4.0.2 on 2022-03-21 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('datetime_created',), 'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
    ]
