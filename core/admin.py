from django.contrib import admin
from .models import Local, Post, PostLike

# Register your models here.
admin.site.register(Post)
admin.site.register(Local)
admin.site.register(PostLike)