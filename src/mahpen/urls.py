"""mahpen URL Configuration

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
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/__debug__/', include('debug_toolbar.urls')),
    path('', include('blog.urls')),
    path('', include('course.urls')),
    path('user/', include('user_management.urls')),
    path('card/', include('zarinpal.urls')),
]

# permission based handler
from user_management.handlers import Handler
handler403 = Handler.as_view()
# handler404 = Handler.as_view()

if settings.DEBUG :
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)