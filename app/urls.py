from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='api/v1/',
        view=include('authentication.urls'),
    ),
    path(
        route='api/v1/',
        view=include('genres.urls'),
    ),
    path(
        route='api/v1/',
        view=include('actors.urls'),
    ),
    path(
        route='api/v1/',
        view=include('movies.urls'),
    ),
    path(
        route='api/v1/',
        view=include('reviews.urls'),
    ),
]
