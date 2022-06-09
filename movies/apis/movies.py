from django.db import models
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from movies.filters.movie_order_filter import MovieOrderFilter
from movies.models import Movie
from movies.paginators.movie_paginator import MoviePagination
from movies.serializers.movie_serializer import MovieSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, MovieOrderFilter]
    search_fields = ["title", "genres"]
    ordering_fields = ["score"]
    queryset = (
        Movie.objects.all()
        .annotate(average_score=models.Avg("review__score"))
        .order_by("id")
    )
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
