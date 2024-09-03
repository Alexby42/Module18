from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class based(TemplateView):
    template_name = 'sample1.html'

class shop(TemplateView):
    template_name = 'sample2.html'

class basket(TemplateView):
    template_name = 'sample3.html'