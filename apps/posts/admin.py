from django.contrib import admin
from .models import Post , Post_Category , PostImages

admin.site.register(Post)

admin.site.register(Post_Category)

admin.site.register(PostImages)