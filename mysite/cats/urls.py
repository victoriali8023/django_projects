from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name='cats'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.CatsCreate.as_view(), name='cats_create'),
    path('main/<int:pk>/update/', views.CatsUpdate.as_view(), name='cats_update'),
    path('main/<int:pk>/delete/', views.CatsDelete.as_view(), name='cats_delete'),
    path('lookup/', views.BreedView.as_view(), name='breed_list'),
    path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]
