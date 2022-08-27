"""djangoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from profiles.views import MyTokenObtainPairView


urlpatterns = [
    path('api/users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/', include('register.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('profiles.urls')),
    path('api/', include('posts.urls')),
]







urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configure Admin Titles
admin.site.site_header = "WeProsper Administration"
admin.site.site_title = "WeProsper Administration"
admin.site.index_title = "Welcome to the WeProsper Administration Area"
