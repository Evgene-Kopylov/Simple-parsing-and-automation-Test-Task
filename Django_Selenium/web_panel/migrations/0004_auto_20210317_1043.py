# Generated by Django 3.1.7 on 2021-03-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_panel', '0003_auto_20210317_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsingresults',
            name='slot_1',
            field=models.CharField(default='', max_length=500, verbose_name='Uptime'),
        ),
        migrations.AlterField(
            model_name='parsingresults',
            name='slot_2',
            field=models.CharField(default='', max_length=500, verbose_name='Fee'),
        ),
        migrations.AlterField(
            model_name='parsingresults',
            name='slot_3',
            field=models.CharField(default='', max_length=500, verbose_name='Teme left'),
        ),
    ]
