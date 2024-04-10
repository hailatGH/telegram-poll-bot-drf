from django.urls import path
from users.views import UserAPIView, UserDetailAPIView, GroupAPIView, GroupDetailAPIView, PermissionAPIView

urlpatterns = [
    path('groups/', GroupAPIView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name='group-detail'),

    path('permissions/', PermissionAPIView.as_view(), name='permission-list'),

    path('users/', UserAPIView.as_view(), name='user-list'),
    path('users/<str:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]