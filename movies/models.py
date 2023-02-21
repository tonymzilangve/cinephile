from datetime import date

from django.contrib.auth.models import User
from django.db import models

from movies.utils import GENRES, GENDER, PRIMARY_ROLES, SECONDARY_ROLES
from django_countries.fields import CountryField

class Movie(models.Model):
    """ Movie """

    title = models.CharField(max_length=50, verbose_name="Movie")
    genre = models.CharField(max_length=30, blank=True, null=True, choices=GENRES, verbose_name="Genre")   # multiple!
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Cat")
    release_date = models.DateField(default=date.today, verbose_name="Premier")
    duration = models.DurationField()  # IntegerField

    actors = models.ManyToManyField('PrimaryCast', related_name="film_actor", verbose_name="Actors")
    director = models.ManyToManyField('PrimaryCast', related_name="film_director", verbose_name="Director")
    operator = models.ManyToManyField('SecondaryCast', blank=True, related_name="film_operator", verbose_name="Operator")
    script = models.ManyToManyField('SecondaryCast', blank=True, related_name="film_script_writer", verbose_name="Script")
    composer = models.ManyToManyField('SecondaryCast', blank=True, related_name="film_composer", verbose_name="Composer")

    poster = models.ImageField(upload_to=f"{title}/posters/", blank=True, null=True, verbose_name="Poster")
    budget = models.PositiveIntegerField(blank=True, null=True)  # verbose = Budget
    box_office = models.PositiveIntegerField(blank=True, null=True)
    awards = models.ManyToManyField('Award', blank=True, verbose_name="Awards")

    review_count = models.PositiveIntegerField(verbose_name="Reviews")

    tagline = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tagline")
    summary = models.TextField(max_length=2000, verbose_name="Summary")
    studio = models.CharField(max_length=100, blank=True, null=True, verbose_name="Studio")

    country = CountryField(multiple=True, verbose_name="Country")   # совместное производство
    # country = models.CharField(max_length=50, choices=COUNTRIES, verbose_name="Country")

    def __str__(self):
        return self.title

    def directors(self):
        return "\n".join([d.name + ',' for d in self.director.all()])

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
    # age = models.IntegerField(verbose_name="Age")
    photo = models.ImageField(upload_to="static/actors_and_directors/", blank=True, null=True, verbose_name="Photo")
    bio = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Bio")
    awards = models.ManyToManyField('Award', blank=True, verbose_name="Awards")

    film_count = models.PositiveIntegerField(default=1, verbose_name="Movies")

    def __str__(self):
        return f"{self.name}({self.role})"

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

    def __str__(self):
        return f"{self.name}({self.role})"

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


class Review(models.Model):
    """ Reviews by professional Cinema Critics """

    text = models.TextField(max_length=3000, verbose_name="Review")
    critic = models.ForeignKey('Critic', on_delete=models.SET_NULL, null=True, verbose_name="Critic")
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name="Movie")

    def __str__(self):
        return f"{self.critic} about {self.movie}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-id']


class Comment(models.Model):
    """ Comments by ordinary users """

    text = models.TextField(max_length=1000, verbose_name="Comment")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Author")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-id']


class RatingStar(models.Model):
    """ Stars of Rating """

    value = models.PositiveSmallIntegerField(default=0, verbose_name="Star")

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Rating Star"
        verbose_name_plural = "Rating Stars"


class Rating(models.Model):
    """ Rating """

    ip = models.CharField(max_length=15)
    star = models.ForeignKey('RatingStar', on_delete=models.CASCADE, verbose_name="Star")
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name="Movie")

    def __str__(self):
        return f"{self.value} stars for {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

