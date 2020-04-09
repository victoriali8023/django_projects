from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name='shows'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.ShowCreate.as_view(), name='show_create'),
    path('main/<int:pk>/update/', views.ShowUpdate.as_view(), name='show_update'),
    path('main/<int:pk>/delete/', views.ShowDelete.as_view(), name='show_delete'),
    path('lookup/', views.TypeView.as_view(), name='type_list'),
    path('lookup/create/', views.TypeCreate.as_view(), name='type_create'),
    path('lookup/<int:pk>/update/', views.TypeUpdate.as_view(), name='type_update'),
    path('lookup/<int:pk>/delete/', views.TypeDelete.as_view(), name='type_delete'),
]
