from django.contrib import admin
from .models import PostModel, ReplyModel

admin.site.register(PostModel)
admin.site.register(ReplyModel)