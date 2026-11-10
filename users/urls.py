from django.urls import path

from users.views import ProfileAPIView, CategoryListCreateAPIView, CategoryDetailUpdateDestroyAPIView, RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),


    #category boshlanadi
    path('cat/', CategoryListCreateAPIView.as_view()),
    path('cat/<int:pk>/', CategoryDetailUpdateDestroyAPIView.as_view()),

]