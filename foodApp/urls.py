"""
URL configuration for foodApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
# Import the global settings of the Django project from settings.py
from django.conf import settings

# Import the 'static' function to handle static and media files
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", include("food.urls")),# see food app url.py
]

# Configuration for serving static and media files during development

if settings.DEBUG:
    
    # Add URLs to serve media files (MEDIA_URL) using the file system path specified in MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
