from movies.models import Movie
from movies.test.base import MoviesBaseTestCase


class PaginationInUnitApiTestCase(MoviesBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.movie = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Action",
            duration="2h",
        )

        self.movie_2 = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 2",
            plot="This is a test 2 plot",
            genres="Action",
            duration="2h",
        )

    def test_response_should_return_all_movies__when_no_page_size_param_and_default_page_size_is_10_for_two_movies(
        self,
    ):
        response = self.client.get("/movies/")

        data = response.data

        self.assertEqual(data["count"], 2)
        self.assertIsNone(data["next"])
        self.assertIsNone(data["previous"])
        self.assertDictEqual(
            {
                 "id": self.movie.pk,
                "image": self.movie.image,
                "title": self.movie.title,
                "plot": self.movie.plot,
                "genres": self.movie.genres,
                "duration": self.movie.duration,
                "score": None,
            },
            data["results"][0],
        )
        self.assertDictEqual(
            {
                 "id": self.movie_2.pk,
                "image": self.movie_2.image,
                "title": self.movie_2.title,
                "plot": self.movie_2.plot,
                "genres": self.movie_2.genres,
                "duration": self.movie_2.duration,
                "score": None,
            },
            data["results"][1],
        )

    def test_response_should_return_first_movie_created__when_given_page_size_param_is_one(
        self,
    ):
        response = self.client.get("/movies/?page_size=1")

        data = response.data

        self.assertEqual(data["count"], 2)

        self.assertIn("/movies/?page=2&page_size=1", data["next"])
        self.assertIsNone(data["previous"])
        self.assertDictEqual(
            {
                "id": self.movie.pk,
                "image": self.movie.image,
                "title": self.movie.title,
                "plot": self.movie.plot,
                "genres": self.movie.genres,
                "duration": self.movie.duration,
                "score": None,
            },
            data["results"][0],
        )

        response = self.client.get(data["next"])

        data = response.data

        self.assertEqual(data["count"], 2)

        self.assertIsNone(data["next"])
        self.assertIn("/movies/?page_size=1", data["previous"])
        self.assertDictEqual(
            {
                "id": self.movie_2.pk,
                "image": self.movie_2.image,
                "title": self.movie_2.title,
                "plot": self.movie_2.plot,
                "genres": self.movie_2.genres,
                "duration": self.movie_2.duration,
                "score": None,
            },
            data["results"][0],
        )
