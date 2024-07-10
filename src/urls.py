"""
URL configuration for src project.

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
from django.urls import path, include
from main.views import *
from leads import views as leads_views
from django.conf import settings
from django.conf.urls.static import static
# urls.py

from django.conf.urls import handler404
from main.views import custom_404_view

handler404 = custom_404_view
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, MyModelSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'mymodel': MyModelSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('base', base , name="home" ),
    path('', include('main.urls')),
    path('form/',include('leads.urls')),
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('contact/', contact_page, name='contact_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    