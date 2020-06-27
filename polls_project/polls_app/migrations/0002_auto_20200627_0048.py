# Generated by Django 3.0.7 on 2020-06-27 00:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='votes',
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]
