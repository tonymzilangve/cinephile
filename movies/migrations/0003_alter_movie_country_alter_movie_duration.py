# Generated by Django 4.1.5 on 2023-04-18 00:36

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=746, multiple=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
