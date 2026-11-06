from django.contrib import admin
from django.urls import path

from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

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
]
