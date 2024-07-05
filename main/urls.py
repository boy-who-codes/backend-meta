from django.urls import path
from .views import  *
from . import views
urlpatterns = [
    path('<slug:slug>/', page_detail, name='page_detail'),
    # path('contact/', views.contact_page, name='contact_page'),
]
