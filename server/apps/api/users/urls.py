from django.urls import path
from .views import (
  UserRegistrationView,
  UserListView,
  UserDetailView,
  UserUpdateView,
  UserHardDeleteView,
  UserSoftDeleteView
)

urlpatterns = [
  path('list/', UserListView.as_view(), name='users-list'),
  path('details/<str:pk>/', UserDetailView.as_view(), name='users-detail'),
  path('register/', UserRegistrationView.as_view(), name='users-register'),
  path('update/<str:pk>/', UserUpdateView.as_view(), name='users-update'),
  path('hard-delete/<str:pk>/', UserHardDeleteView.as_view(), name='users-delete'),
  path('soft-delete/<str:pk>/', UserSoftDeleteView.as_view(), name='users-delete'),
]