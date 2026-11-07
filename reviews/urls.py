from django.urls import path

from . import views

urlpatterns = [
    path(
        route='reviews/',
        view=views.ReviewCreateListView.as_view(),
        name='review-create-list',
    ),
    path(
        route='reviews/<int:pk>/',
        view=views.ReviewRetrieveUpdateDestroyView.as_view(),
        name='review-detail-view',
    ),
]
