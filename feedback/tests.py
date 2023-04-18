from django.contrib.auth import get_user_model
from django.test import TestCase

from feedback.models import Review, Comment, RatingStar, Rating
from movies.models import Movie, Critic


def create_user():
    """ Creates a test user """

    db = get_user_model()
    user = db.objects.create_user(
        'test@user.com', 'username', 'password')
    return user


class FeedbackModelTest(TestCase):
    """ Class for testing Feedback models """

    def create_movie(self):
        sample_movie = Movie.objects.create(
            title='sample_movie',
            summary='sample_movie_summary',
        )
        return sample_movie

    def create_review(self):
        critic = Critic.objects.create(name='sample_critic')
        review = Review.objects.create(
            text='sample_text',
            movie=self.create_movie(),
            critic=critic,
        )
        return review

    def test_review(self):
        review = self.create_review()
        self.assertEqual(review.__str__(), f"{review.critic} about {review.movie}")

    def test_comment(self):
        review = self.create_review()
        comment = Comment.objects.create(
            text='sample_comment',
            author=create_user(),
            object_id=1,          # was ist? Ich brauche review!
            content_type_id=review.id,   # ContentType   // 1
        )
        self.assertEqual(comment.__str__(), f"Comment №{comment.id} by {comment.author}")
        self.assertEqual(review.total_comments(), 1)

    def test_rating_star(self):
        star = RatingStar.objects.create()
        self.assertEqual(star.__str__(), str(star.value))

    def test_rating(self):
        rating = Rating.objects.create(
            ip='sample_ip',
            star=RatingStar.objects.create(),
            movie=self.create_movie(),
        )
        print(rating.__str__())
        self.assertEqual(rating.__str__(), f"{rating.star} stars for {rating.movie}")
