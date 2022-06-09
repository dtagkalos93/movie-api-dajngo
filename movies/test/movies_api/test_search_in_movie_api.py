from movies.models import Movie
from movies.test.base import MoviesBaseTestCase


class SearchUnitApiTestCase(MoviesBaseTestCase):
    def test_should_return_data_with_specific_genres_when_searching_with_genres(self):
        movie = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Action",
            duration="2h",
        )
        Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Adventure",
            duration="2h",
        )
        response = self.client.get("/movies/?search=Action")

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

    def test_should_return_data_with_specific_title_when_searching_with_title(self):
        movie = Movie.objects.create(
            image="foo/bar.gr",
            title="Test 1",
            plot="This is a test plot",
            genres="Action",
            duration="2h",
        )
        Movie.objects.create(
            image="foo/bar.gr",
            title="Test 2",
            plot="This is a test plot",
            genres="Adventure",
            duration="2h",
        )
        response = self.client.get("/movies/?search=Test 1")

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
