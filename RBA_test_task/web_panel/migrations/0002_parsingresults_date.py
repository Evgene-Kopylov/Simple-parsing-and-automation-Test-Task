# Generated by Django 3.1.7 on 2021-03-16 23:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parsingresults',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
    ]
