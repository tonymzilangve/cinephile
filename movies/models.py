from datetime import date

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from django.db import models
from django.db.models import Q

# from feedback.models import Comment
from embed_video.fields import EmbedVideoField

from movies.utils import GENRES, GENDER, PRIMARY_ROLES, SECONDARY_ROLES
from django_countries.fields import CountryField


# def user_directory_path1(instance, filename):
#     # today = datetime.now().date()
#     # today_path = today.strftime("%Y/%m/%d")
#     return f'{instance.title}/posters/{filename}'
# upload_to=user_directory_path1


class Movie(models.Model):
    """ Movie """

    title = models.CharField(max_length=50, verbose_name="Movie")
    genre = models.CharField(max_length=30, blank=True, null=True, choices=GENRES, verbose_name="Genre")   # multiple!
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Cat")
    release_date = models.DateField(default=date.today, verbose_name="Premier")
    duration = models.DurationField(blank=True, null=True)  # IntegerField
    # come scrivere este formato?

    actors = models.ManyToManyField('PrimaryCast', related_name="film_actor", verbose_name="Actors")
    director = models.ManyToManyField('PrimaryCast', related_name="film_director", verbose_name="Director")
    operator = models.ManyToManyField('SecondaryCast', blank=True, related_name="film_operator", verbose_name="Operator")
    script = models.ManyToManyField('SecondaryCast', blank=True, related_name="film_script_writer", verbose_name="Script")
    composer = models.ManyToManyField('SecondaryCast', blank=True, related_name="film_composer", verbose_name="Composer")

    poster = models.ImageField(upload_to=f"{title}/posters/", blank=True, null=True, verbose_name="Poster")
    budget = models.PositiveIntegerField(blank=True, null=True)  # verbose = Budget
    box_office = models.PositiveIntegerField(blank=True, null=True)
    awards = models.ManyToManyField('Award', blank=True, verbose_name="Awards")

    # review_count = models.PositiveIntegerField(verbose_name="Reviews")
    # вывод в admin через property?

    tagline = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tagline")
    summary = models.TextField(max_length=2000, verbose_name="Summary")
    studio = models.CharField(max_length=100, blank=True, null=True, verbose_name="Studio")

    trailer = EmbedVideoField(blank=True, null=True, verbose_name='Trailer')
    country = CountryField(multiple=True, blank=True, verbose_name="Country")   # совместное производство
    # country = models.CharField(max_length=50, choices=COUNTRIES, verbose_name="Country")

    # comments = fields.GenericRelation(Comment)

    def __str__(self):
        return self.title

    def directors(self):
        return "\n".join([d.name + ',' for d in self.director.all()])

    # @property # -> обеспечит постоянное обновление??
    def total_reviews(self):
        return self.reviews.all().count()

    def total_comments(self):
        return self.comments.all().count()

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['-release_date']


class Category(models.Model):
    """ Film Category """

    name = models.CharField(max_length=100, verbose_name="Category")
    desc = models.TextField(max_length=1000, verbose_name="Description")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class PrimaryCast(models.Model):
    """ Actors & Film Directors """

    role = models.CharField(max_length=50, choices=PRIMARY_ROLES, verbose_name="Role")
    name = models.CharField(max_length=100, verbose_name="Actor"),
    gender = models.CharField(max_length=10, choices=GENDER, verbose_name="Gender")
    birthday = models.DateField(verbose_name="Born")   # datetime.now().date - birthday
    citizenship = CountryField(multiple=True, verbose_name="Country")
    # citizenship = models.CharField(max_length=50, blank=True, null=True, choices=COUNTRIES, verbose_name="Country")
    # age = models.IntegerField(verbose_name="Age")   # from birthday
    photo = models.ImageField(upload_to="static/actors_and_directors/", blank=True, null=True, verbose_name="Photo")
    bio = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Bio")
    awards = models.ManyToManyField('Award', blank=True, verbose_name="Awards")

    # film_count = models.PositiveIntegerField(default=1, verbose_name="Movies")

    def __str__(self):
        return f"{self.name}({self.role})"

    # через self.role ->чтобы не перебирать всевозможные варианты
    @property
    def total_films(self):
        return Movie.objects.filter(Q(actors__role=self.id) | Q(director__role=self.id)).distinct().count()

    class Meta:
        verbose_name = 'Actor / Director'
        verbose_name_plural = 'Actors / Directors'
        ordering = ['role']


class SecondaryCast(models.Model):
    """ Script writer / Operator / Composer """

    role = models.CharField(max_length=50, choices=SECONDARY_ROLES, verbose_name="Role")
    name = models.CharField(max_length=50, verbose_name="Director")
    gender = models.CharField(max_length=10, choices=GENDER, verbose_name="Gender")
    citizenship = CountryField(multiple=True, verbose_name="Country")
    # citizenship = models.CharField(max_length=50, blank=True, null=True, choices=COUNTRIES, verbose_name="Country")

    awards = models.ManyToManyField('Award', blank=True, verbose_name="Awards")

    def __str__(self):
        return f"{self.name}({self.role})"

    @property
    def total_films(self):
        return Movie.objects.filter(Q(operator__role=self.id)
                                    | Q(script__role=self.id)
                                    | Q(composer__role=self.id)).distinct().count()

    class Meta:
        verbose_name = 'Other Role'
        verbose_name_plural = 'Other Roles'
        ordering = ['role']


class MovieShot(models.Model):
    """ Shots from Movie """

    desc = models.CharField(max_length=100, verbose_name="Description")
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name="shots", verbose_name="Movie")
    shot = models.ImageField(upload_to=f"{movie}/shots", verbose_name="Shot")

    def __str__(self):
        return str(self.movie) + "'s shots"

    class Meta:
        verbose_name = 'Shot'
        verbose_name_plural = 'Shots'
        ordering = ['movie']


class Award(models.Model):
    """ Award & Honours """

    name = models.CharField(max_length=50, verbose_name="Award")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'
        ordering = ['name']


class Critic(models.Model):
    """ Professional Cinema Critic """

    name = models.CharField(max_length=50, verbose_name="Critic")
    # rating  Float

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Critic'
        verbose_name_plural = 'Critics'
        ordering = ['name']

