from django.urls import path
from .views import PxProfundidadeView, PxTempoView

urlpatterns = [
    path('profundidade/', PxProfundidadeView.as_view(), name='PxProfundidade'),
    path('tempo/', PxTempoView.as_view(), name='PxTempo')
]
