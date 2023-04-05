from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields

from django.db import models
from django.contrib.auth.models import User

from movies.models import Movie, Critic
from my_auth.models import CustomUser


class Review(models.Model):
    """ Reviews by professional Cinema Critics """

    text = models.TextField(max_length=3000, verbose_name="Review")
    critic = models.ForeignKey(Critic, on_delete=models.SET_NULL, null=True, verbose_name="Critic")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', verbose_name="Movie")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    comments = fields.GenericRelation('Comment')

    # rating??? (moyenne)

    def __str__(self):
        return f"{self.critic} about {self.movie}"

    def total_comments(self):
        return self.comments.all().count()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-id']


class Comment(models.Model):
    """ Comments by ordinary users """

    text = models.TextField(max_length=1000, verbose_name="Comment")
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='comments', verbose_name="Author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name='likes', verbose_name='Лайкнули')   # number or Users
    dislikes = models.ManyToManyField(CustomUser, related_name='dislikes', verbose_name='Лайкнули')

    content_type = models.ForeignKey(ContentType, related_name='comments', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Comment №{self.id} by {self.author}"

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
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie")

    def __str__(self):
        return f"{self.star} stars for {self.movie}"   # value

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
