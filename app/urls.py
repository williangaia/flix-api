from django.contrib import admin
from django.urls import path

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
]
