from django.contrib import admin
from django.urls import path

from genres.views import genre_create_list_view, genre_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='genres/', view=genre_create_list_view, name='genre-create-list'
    ),
    path(
        route='genres/<int:pk>/',
        view=genre_detail_view,
        name='genre-detail-view',
    ),
]
