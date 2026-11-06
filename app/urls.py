from django.contrib import admin
from django.urls import path

from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='genres/',
        view=GenreCreateListView.as_view(),
        name='genre-create-list',
    ),
    path(
        route='genres/<int:pk>/',
        view=GenreRetrieveUpdateDestroyView.as_view(),
        name='genre-detail-view',
    ),
    path(
        route='actors/',
        view=ActorCreateListView.as_view(),
        name='actor-create-list',
    ),
    path(
        route='actors/<int:pk>/',
        view=ActorRetrieveUpdateDestroyView.as_view(),
        name='actor-detail-view',
    ),
    path(
        route='movies/',
        view=MovieCreateListView.as_view(),
        name='movie-create-list',
    ),
    path(
        route='movies/<int:pk>/',
        view=MovieRetrieveUpdateDestroyView.as_view(),
        name='movie-detail-view',
    ),
    path(
        route='reviews/',
        view=ReviewCreateListView.as_view(),
        name='review-create-list',
    ),
    path(
        route='reviews/<int:pk>/',
        view=ReviewRetrieveUpdateDestroyView.as_view(),
        name='review-detail-view',
    ),
]
