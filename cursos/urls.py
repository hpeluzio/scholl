from django.urls import path

from .views import CursoAPIView, AvaliacaoAPIView

urlpatterns = [
  path('cursos/', CursoAPIView.as_views(), name='cursos')
  path('avaliacoes/', AvaliacaoAPIView.as_views(), name='avaliacoes')
]