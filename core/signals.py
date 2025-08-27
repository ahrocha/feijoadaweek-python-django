# core/signals.py
from django.dispatch import receiver
from django_comments.signals import comment_will_be_posted

@receiver(comment_will_be_posted)
def always_hold_for_moderation(sender, comment, request, **kwargs):
    comment.is_public = False
    return True
