from movies.models import Movie, Review
from movies.test.base import MoviesBaseTestCase


class OrderInMovieApiTestCase(MoviesBaseTestCase):
    def setUp(self) -> None:
        super(OrderInMovieApiTestCase, self).setUp()
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
        self.review = Review.objects.create(movie=self.movie, score=4)
        self.review_2 = Review.objects.create(movie=self.movie_2, score=5)

    def test_response_should_return_with_asc_score_when_requested_asc_score(self):
        response = self.client.get("/movies/?ordering=score")

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
                "score": "%0.2f" % (self.review.score,),
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
                "score": "%0.2f" % (self.review_2.score,),
            },
            data["results"][1],
        )

    def test_response_should_return_with_desc_score_when_requested_desc_score(self):
        response = self.client.get("/movies/?ordering=-score")

        data = response.data

        self.assertEqual(data["count"], 2)
        self.assertIsNone(data["next"])
        self.assertIsNone(data["previous"])
        self.assertDictEqual(
            {
                "id": self.movie_2.pk,
                "image": self.movie_2.image,
                "title": self.movie_2.title,
                "plot": self.movie_2.plot,
                "genres": self.movie_2.genres,
                "duration": self.movie_2.duration,
                "score": "%0.2f" % (self.review_2.score,),
            },
            data["results"][0],
        )
        self.assertDictEqual(
            {
                "id": self.movie.pk,
                "image": self.movie.image,
                "title": self.movie.title,
                "region": self.movie.region,
                "description": self.movie.description,
                "cancellation": self.movie.cancellation,
                "price": self.movie.price,
                "score": "%0.2f" % (self.review.score,),
            },
            data["results"][1],
        )
