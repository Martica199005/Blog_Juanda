# Generated by Django 3.0.2 on 2020-04-01 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200401_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='type',
        ),
    ]
