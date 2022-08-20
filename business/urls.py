from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import BusinessViewSet


router = routers.DefaultRouter()
router.register('business', BusinessViewSet)


urlpatterns = [
    path('', include(router.urls)),
]