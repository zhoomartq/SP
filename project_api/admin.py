from django.contrib import admin

from project_api.models import Post, Like, DisLike

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(DisLike)
