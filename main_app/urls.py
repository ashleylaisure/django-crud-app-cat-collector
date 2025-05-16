from django.urls import path
from . import views

urlpatterns = [
    # we are going to define all app-level urls in this list
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]