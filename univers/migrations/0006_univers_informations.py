# Generated by Django 3.1 on 2020-08-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univers', '0005_auto_20200819_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='univers',
            name='informations',
            field=models.SmallIntegerField(default=0),
        ),
    ]
