from . import views
from django.urls import path

urlpatterns = [
  path('', views.inicio, name="Inicio"),
  path('familias', views.familias, name="Familias"),
]