# Generated by Django 3.1 on 2020-08-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univers', '0007_auto_20200820_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='univers',
            name='aProposDeLaChanson',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='univers',
            name='aProposDuFilm',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='univers',
            name='aProposDuLivre',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='univers',
            name='chansonPreferee',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='univers',
            name='filmPrefere',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='univers',
            name='livrePrefere',
            field=models.CharField(max_length=100, null=True),
        ),
    ]