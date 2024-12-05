"""
URL configuration for AppointmentSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from Settings import views
from django.views.static import serve

handler404 = views.custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='', view=include('Appointments.urls')),
    path(route='hakkimizda/', view=include('About.urls')),
    path(route='kullanici/', view=include('User.urls')),
    path(route='iletisim/', view=include('Contact.urls')),
]

if not settings.DEBUG:
    
    urlpatterns += re_path(
       r'^static/(?P<path>.*)$', serve, dict(document_root=settings.STATIC_ROOT)),
    urlpatterns += re_path(
       r'^media/(?P<path>.*)$', serve, dict(document_root=settings.MEDIA_ROOT)),
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)