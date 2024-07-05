from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('Complications-and-verification-process/', views.lead_form, name='lead_form'),
    path('lead-list/', views.lead_list, name='lead_list'),
]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)