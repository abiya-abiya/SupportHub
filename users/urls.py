from django.urls import path

from users.views import RegisterAPI, LoginAPI, RefreshTokenAPIView, ProfileAPIView

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('token/refresh/', RefreshTokenAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
]