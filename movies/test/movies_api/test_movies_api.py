from django.test import Client
from rest_framework import status


from movies.models import Movie, Review
from movies.test.base import MoviesBaseTestCase


class MoviesApiTestCase(MoviesBaseTestCase):
    def test_movie_api_should_get_401_when_jwt_not_given(self):
        Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Action",
            duration="2h",

        )
        response = Client().get("/movies/")

        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_movie_api_should_return_correct_response_when_data_exist(self):
        movie = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Action",
            duration="2h",
        )
        response = self.client.get("/movies/")

        data = response.data
        self.assertEqual(data["count"], 1)
        self.assertIsNone(data["next"])
        self.assertIsNone(data["previous"])
        self.assertDictEqual(
            {
                "id": movie.pk,
                "image": movie.image,
                "title": movie.title,
                "plot": movie.plot,
                "genres": movie.genres,
                "duration": movie.duration,
                "score": None,
            },
            data["results"][0],
        )

    def test_movie_api_should_return_empty_response_when_no_data_exist(self):
        response = self.client.get("/movies/")
        data = response.data
        self.assertEqual(data["count"], 0)
        self.assertIsNone(data["next"])
        self.assertIsNone(data["previous"])
        self.assertEqual([], data["results"])

    def test_movie_api_should_return_correct_response_when_unit_exist_with_one_review(
        self,
    ):
        movie = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Action"
        )
        review = Review.objects.create(movie=movie, score=4)
        response = self.client.get("/movies/")

        data = response.data
        self.assertEqual(data["count"], 1)
        self.assertIsNone(data["next"])
        self.assertIsNone(data["previous"])
        self.assertDictEqual(
            {
                "id": movie.pk,
                "image": movie.image,
                "title": movie.title,
                "plot": movie.plot,
                "genres": movie.genres,
                "duration": movie.duration,
                "score": "%0.2f" % (review.score),
            },
            data["results"][0],
        )

    def test_movie_api_should_return_correct_response_with_average_score_when_unit_exist_with_two_review(
        self,
    ):
        movie = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Action"
        )
        review = Review.objects.create(movie=movie, score=4)
        review_2 = Review.objects.create(movie=movie, score=5)

        response = self.client.get("/movies/")

        data = response.data

        expected_average_score = (review.score + review_2.score) / 2.0
        self.assertEqual(data["count"], 1)
        self.assertIsNone(data["next"])
        self.assertIsNone(data["previous"])
        self.assertDictEqual(
            {
                "id": movie.pk,
                "image": movie.image,
                "title": movie.title,
                "plot": movie.plot,
                "genres": movie.genres,
                "duration": movie.duration,
                "score": "%0.2f" % (expected_average_score,),
            },
            data["results"][0],
        )
