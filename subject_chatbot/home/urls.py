from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='home-landing'),
    path('about/', views.about_view, name='home-about'),
]
