from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import PostViewSet, ReplyViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('replies', ReplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
