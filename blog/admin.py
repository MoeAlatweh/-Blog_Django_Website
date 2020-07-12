from django.contrib import admin
# import Post, and Comment from model file
from .models import Post, Comment

# Register your models here.

# Register post models
admin.site.register(Post)

# Register post models
admin.site.register(Comment)