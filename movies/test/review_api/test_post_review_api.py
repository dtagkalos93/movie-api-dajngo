from django.test import Client
from rest_framework import status

from movies.models import Movie, Review
from movies.test.base import MoviesBaseTestCase


class PostReviewApiTestCase(MoviesBaseTestCase):
    def test_post_should_get_unauthorized_if_jwt_token_is_missing(self):
        movie = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Action",
            duration="2h",
        )
        response = Client().post(
            "/review/",
            {"score": 4, "comment": "This is a test review", "movie": movie.pk},
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_review_api_for_movie_should_import_correct(self):
        movie = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Action",
            duration="2h",
        )
        response = self.client.post(
            "/review/",
            {"score": 4, "comment": "This is a test review", "movie": movie.pk},
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.data,
            {"score": 4, "comment": "This is a test review", "movie": movie.pk},
        )
        review = Review.objects.get(movie=movie)
        self.assertEqual(review.score, 4)
        self.assertEqual(review.comment, "This is a test review")

    def test_post_review_api_for_movie_with_score_greater_than_five_should_failed_and_return_bad_request(
        self,
    ):
        movie = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            genres="Action",
            duration="2h",
        )
        response = self.client.post("/review/", {"score": 10, "unit": movie.pk})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.data["score"][0].title(),
            "Ensure This Value Is Less Than Or Equal To 5.",
        )

    def test_post_review_api_for_movie_that_not_exist_should_return_bad_reqeust(self):
        response = self.client.post("/review/", {"score": 3, "movie": 3})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.data["movie"][0].title(), 'Invalid Pk "3" - Object Does Not Exist.'
        )
