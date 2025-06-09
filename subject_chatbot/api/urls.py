from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_api_view, name='api_chat'),
    path('catalog/', views.catalog_api_view, name='api_catalog'),
]
