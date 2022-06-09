from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from movies.models import Review
from movies.serializers.review_serializer import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
