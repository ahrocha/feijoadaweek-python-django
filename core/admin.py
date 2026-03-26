from django.contrib import admin
from .models import Post, PostLike

# Register your models here.
admin.site.register(Post)
admin.site.register(PostLike)