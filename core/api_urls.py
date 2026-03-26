from django.urls import path
from .viewsets import PostLikeAPIView

app_name = 'api'

urlpatterns = [
    path('posts/<int:pk>/like/', PostLikeAPIView.as_view(), name='post-like'),
]
