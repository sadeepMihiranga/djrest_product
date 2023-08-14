from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UnileverUserCreate

from authentication.views import CustomTokenObtainPairView

urlpatterns = [
    # path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # access token with basic info
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), # access token with additional info
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/user/create/', UnileverUserCreate.as_view(), name="create_user"),
]
