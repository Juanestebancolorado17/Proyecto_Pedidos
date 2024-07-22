from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('table/', views.table, name='table'),
    path('filtrar/<str:categoria>/', views.filtrar_por_categoria, name='filtrar_por_categoria'),

]

