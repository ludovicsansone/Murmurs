# Generated by Django 3.1 on 2020-08-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univers', '0006_univers_informations'),
    ]

    operations = [
        migrations.AddField(
            model_name='univers',
            name='recherche',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='univers',
            name='villeDeResidence',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
