from random import randrange

from django.core.management import BaseCommand

from account.models import User
from movies.models import Movie, Review


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Importing Test Data")
        self.create_users()
        genres = [
            "ACTION",
            "ADVENTURE",
            "THRILLER",
        ]
        self.create_movies_with_out_reviews(genres)
        self.create_movies_with_reviews(genres)
        print("Test Data have been imported")

    @staticmethod
    def create_users():
        for x in range(1, 4):
            User.objects.create_user(username=f"viewer_{x}", password="tempass1234!")

    @staticmethod
    def create_movies_with_out_reviews(genres):
        title = [
            "Batman",
            "Superman",
            "Wonder Woman",
        ]
        for x in range(0, 3):
            Movie.objects.create(
                image=f"foo/bar{x}.jpg",
                title=title[x],
                genres=genres[x],
                plot="This is a test plot",
                duration="2h",
            )

    def create_movies_with_reviews(self, genres):
        title = [
            "Iron Man",
            "Captain America",
            "Thor",
        ]
        for x in range(0, 3):
            movie = Movie.objects.create(
                image=f"foo/bar{x}.jpg",
                title=title[x],
                genres=genres[x],
                plot="This is a test plot",
                duration="2h",
            )
            self.create_review(movie=movie, title=title[x])

    @staticmethod
    def create_review(movie, title):
        for x in range(0, 5):
            Review.objects.create(
                movie=movie, score=randrange(1, 6), comment=f"test comment for {title}"
            )
