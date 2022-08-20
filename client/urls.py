from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ClientViewSet, NotesViewSet


router = routers.DefaultRouter()
router.register('clients', ClientViewSet)
router.register('notes', NotesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]