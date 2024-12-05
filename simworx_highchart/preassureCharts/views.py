from django.shortcuts import render
from django.views.generic import TemplateView

class PxProfundidadeView(TemplateView):
    template_name = 'pCharts/pXprofundidade.html'


class PxTempoView(TemplateView):
    template_name = 'pCharts/pXtempo.html'