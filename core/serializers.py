from rest_framework import serializers
from .models import PostLike, Post


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'post', 'ip_address', 'created_at']
        read_only_fields = ['id', 'created_at']


class PostLikeStatsSerializer(serializers.Serializer):
    """Serializar estatísticas de likes de um post"""
    post_id = serializers.IntegerField()
    like_count = serializers.IntegerField()
    liked = serializers.BooleanField()
