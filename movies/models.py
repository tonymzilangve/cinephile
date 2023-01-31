from django.db import models

from movies.utils import GENRES, COUNTRIES


class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name="Movie")
    genre = models.CharField(max_length=30, blank=True, null=True, choices=GENRES, verbose_name="Genre")   # M2M
    release_date = models.DateField(verbose_name="Premier")
    duration = models.DurationField()  # IntegerField

    actors = models.ManyToManyField('Actor', verbose_name="Actors")
    director = models.ManyToManyField('Director', verbose_name="Director")
    operator = models.ManyToManyField('Operator', verbose_name="Operator")
    script = models.ManyToManyField('ScriptWriter', verbose_name="Script")
    composer = models.ManyToManyField('Composer', verbose_name="Composer")

    poster = models.ImageField(upload_to=f"static/{name}/poster", blank=True, null=True, verbose_name="Poster")
    budget = models.PositiveIntegerField(blank=True, null=True)
    box_office = models.PositiveIntegerField(blank=True, null=True)
    awards = models.ManyToManyField('Award', blank=True, null=True, verbose_name="Awards")

    # reviews = models.    related_name
    review_count = models.PositiveIntegerField(verbose_name="Reviews")
    # rating = models.

    tagline = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tagline")
    summary = models.TextField(max_length=2000, verbose_name="Summary")
    studio = models.CharField(blank=True, null=True, verbose_name="Studio")
    country = models.CharField(max_length=50, choices=COUNTRIES, verbose_name="Country")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['name']


class Actor(models.Model):
    name = models.CharField(max_length=30, verbose_name="Actor"),
    gender = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')), verbose_name="Gender")
    birthday = models.DateField(verbose_name="Born")   # datetime.now().date - birthday
    citizenship = models.CharField(max_length=50, blank=True, null=True, choices=COUNTRIES, verbose_name="Country")
    # age = models.IntegerField(verbose_name="Age")
    photo = models.ImageField(upload_to="static/actors", blank=True, null=True, verbose_name="Photo")
    bio = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Bio")
    awards = models.ManyToManyField('Award', blank=True, verbose_name="Awards")

    film_count = models.PositiveIntegerField(default=1, verbose_name="Movies")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actor / Actress'
        verbose_name_plural = 'Actors / Actresses'


class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name="Director")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'
        ordering = ['name']


class Operator(models.Model):
    name = models.CharField(max_length=50, verbose_name="Operator")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Operator'
        verbose_name_plural = 'Operators'
        ordering = ['name']


class ScriptWriter(models.Model):
    name = models.CharField(max_length=50, verbose_name="Script writer")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Script writer'
        verbose_name_plural = 'Script writers'
        ordering = ['name']


class Composer(models.Model):
    name = models.CharField(max_length=50, verbose_name="Composer")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Composer'
        verbose_name_plural = 'Composers'
        ordering = ['name']


class MovieShot(models.Model):
    desc = models.CharField(max_length=100, verbose_name="Description")
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name="shots", verbose_name="Movie")
    shot = models.ImageField(upload_to=f"static/{movie}/shots", verbose_name="Shot")

    def __str__(self):
        return str(self.movie) + "'s shots"

    class Meta:
        verbose_name = 'Shot'
        verbose_name_plural = 'Shots'
        ordering = ['movie']


class Award(models.Model):
    name = models.CharField(max_length=50, verbose_name="Award")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'
        ordering = ['name']


class Critic(models.Model):
    name = models.CharField(max_length=50, verbose_name="Critic")
    # rating
    #

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Critic'
        verbose_name_plural = 'Critics'
        ordering = ['name']


class Review(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Review")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-id']


class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Comment")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-id']
