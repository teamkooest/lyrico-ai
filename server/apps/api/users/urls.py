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
    # Any (for both admins and clients)
    path('list/', UserListView.as_view(), name='users-list'),
    path('details/<str:pk>/', UserDetailView.as_view(), name='users-detail'),

    # Admins
    path('a/hard-delete/<str:pk>/', UserHardDeleteView.as_view(), name='users-admins-delete'),

    # Clients
    path('c/register/', UserRegistrationView.as_view(), name='users-clients-register'),
    path('c/update/<str:pk>/', UserUpdateView.as_view(), name='users-clients-update'),
    path('c/soft-delete/<str:pk>/', UserSoftDeleteView.as_view(), name='users-clients-delete'),
]