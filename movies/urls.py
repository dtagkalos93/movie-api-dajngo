from rest_framework.routers import DefaultRouter

from movies import apis as api

router = DefaultRouter()
router.register(r"movies", api.MoviesViewSet, basename="movies")
router.register(r"review", api.ReviewViewSet, basename="review-unit")

urlpatterns = router.urls
