from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path(
        route='authentication/token/',
        view=TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        route='authentication/token/refresh/',
        view=TokenRefreshView.as_view(),
        name='token-refresh',
    ),
    path(
        route='authentication/token/verify/',
        view=TokenVerifyView.as_view(),
        name='token_verify',
    ),
]
