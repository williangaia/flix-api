from django.contrib import admin
from django.urls import path

from genres.views import genre_create_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='genres/', view=genre_create_list_view, name='genre-create-list'
    ),
]
