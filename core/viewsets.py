from django.utils import timezone
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from .models import Post, PostLike
from .serializers import PostLikeStatsSerializer


def get_client_ip(request):
    """
    Extrai o IP do cliente, considerando proxies (X-Forwarded-For).
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def check_rate_limit(post_id, ip_address):
    """
    Verifica se o IP pode fazer like no post (máximo 1 por minuto).
    Retorna True se dentro do rate limit, False se violou.
    """
    one_minute_ago = timezone.now() - timedelta(seconds=60)
    recent_like = PostLike.objects.filter(
        post_id=post_id,
        ip_address=ip_address,
        created_at__gte=one_minute_ago
    ).exists()
    return not recent_like


class PostLikeAPIView(APIView):
    """
    API endpoint para gerenciar likes em posts.
    GET /api/posts/<id>/like/ - Retorna contagem de likes
    POST /api/posts/<id>/like/ - Toggle like (adiciona ou remove)
    """

    def get(self, request, pk):
        """Retorna contagem de likes do post"""
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response(
                {'error': 'Post not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        like_count = post.likes.count()
        ip_address = get_client_ip(request)
        user_has_liked = post.likes.filter(ip_address=ip_address).exists()

        data = {
            'post_id': post.id,
            'like_count': like_count,
            'liked': user_has_liked,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Toggle like: adiciona ou remove like baseado em IP"""
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response(
                {'error': 'Post not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        ip_address = get_client_ip(request)

        # Verifica rate limit
        if not check_rate_limit(post.id, ip_address):
            return Response(
                {'error': 'Rate limit exceeded. You can only like once per minute.'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        # Verifica se já existe like
        like = post.likes.filter(ip_address=ip_address).first()

        if like:
            # Remove like (unlike)
            like.delete()
            user_liked = False
            message = 'Like removed'
        else:
            # Adiciona like
            PostLike.objects.create(post=post, ip_address=ip_address)
            user_liked = True
            message = 'Like added'

        like_count = post.likes.count()

        data = {
            'post_id': post.id,
            'like_count': like_count,
            'liked': user_liked,
            'message': message,
        }
        return Response(data, status=status.HTTP_200_OK)
