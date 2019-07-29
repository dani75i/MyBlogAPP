from django.contrib import admin

from blog.models import Post, AllPosts

admin.site.register(Post)
admin.site.register(AllPosts)
