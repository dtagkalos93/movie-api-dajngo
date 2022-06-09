from rest_framework import serializers

from movies.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(required=False)

    class Meta:
        model = Review
        fields = ("score", "comment", "movie")
