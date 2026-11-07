from django.urls import path

from . import views

urlpatterns = [
    path(
        route='actors/',
        view=views.ActorCreateListView.as_view(),
        name='actor-create-list',
    ),
    path(
        route='actors/<int:pk>/',
        view=views.ActorRetrieveUpdateDestroyView.as_view(),
        name='actor-detail-view',
    ),
]
