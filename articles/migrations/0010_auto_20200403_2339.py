# Generated by Django 3.0.2 on 2020-04-03 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_articles_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
