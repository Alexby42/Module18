from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class based(TemplateView):
    template_name = 'third_task/sample1.html'

class shop(TemplateView):
    template_name = 'third_task/sample2.html'

class basket(TemplateView):
    template_name = 'third_task/sample3.html'