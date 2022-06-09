from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    score = serializers.DecimalField(
        max_digits=3, decimal_places=2, source="average_score"
    )

    class Meta:
        model = Movie
        fields = ("id", "image", "title", "plot", "genres", "duration", "score")
