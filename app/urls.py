from django.contrib import admin
from django.urls import path

from genres.views import GenreCreateListView, genre_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='genres/',
        view=GenreCreateListView.as_view(),
        name='genre-create-list',
    ),
    path(
        route='genres/<int:pk>/',
        view=genre_detail_view,
        name='genre-detail-view',
    ),
]
