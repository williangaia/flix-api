from django.urls import path

from . import views

urlpatterns = [
    path(
        route='movies/',
        view=views.MovieCreateListView.as_view(),
        name='movie-create-list',
    ),
    path(
        route='movies/<int:pk>/',
        view=views.MovieRetrieveUpdateDestroyView.as_view(),
        name='movie-detail-view',
    ),
]
