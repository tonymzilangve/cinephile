# Generated by Django 4.1.5 on 2023-04-12 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_trailer'),
        ('feedback', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='tone',
            field=models.CharField(choices=[('Positive', 'positive'), ('Neutral', 'neutral'), ('Negative', 'negative')], default='Positive', max_length=100, verbose_name='Tone'),
        ),
        migrations.AlterField(
            model_name='review',
            name='critic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='movies.critic', verbose_name='Critic'),
        ),
    ]
