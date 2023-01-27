from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name="Movie")
    duration = models.DurationField()  # IntegerField
    actors = models.ManyToManyField('Actor', verbose_name="actors")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['name']


class Actor(models.Model):
    name = models.CharField(max_length=30, verbose_name="name"),
    gender = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')), verbose_name="gender")
    birthday = models.DateField()
    age = models.IntegerField(verbose_name="age")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actor / Actress'
        verbose_name_plural = 'Actors / Actresses'
