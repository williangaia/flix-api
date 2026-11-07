from django.urls import path

from . import views

urlpatterns = [
    path(
        route='genres/',
        view=views.GenreCreateListView.as_view(),
        name='genre-create-list',
    ),
    path(
        route='genres/<int:pk>/',
        view=views.GenreRetrieveUpdateDestroyView.as_view(),
        name='genre-detail-view',
    ),
]
