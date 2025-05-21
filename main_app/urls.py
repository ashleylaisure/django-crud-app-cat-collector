from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # we are going to define all app-level urls in this list
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name="cat-index"),
]