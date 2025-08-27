# core/moderation.py
from django_comments.moderation import CommentModerator, moderator
from .models import Post   # ou o model que você usa para receber comentários

class PostCommentModerator(CommentModerator):
    # todos os comentários entram em moderação
    moderate_after = 0
    enable_field = 'enable_comments'
    # email_notification = True  # opcional

# registra o moderador para o model Post
moderator.register(Post, PostCommentModerator)
