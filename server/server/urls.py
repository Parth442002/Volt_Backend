"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import static
from django.conf import settings  # to import static in deployment
from django.views.static import serve

static_urlpatterns = [
    path("media/", serve, {"document_root": settings.MEDIA_ROOT}),
    path("static/", serve,
         {"document_root": settings.STATIC_ROOT}),
]

urlpatterns = [
    path("", include(static_urlpatterns)),
    path('admin/', admin.site.urls),

    # Authentication Urls
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1auth/registration/', include('dj_rest_auth.registration.urls')),


    # garage urls
    path('api/v1/', include('garage.urls')),
]
