from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class based(TemplateView):
    template_name = 'fourth_task/sample1.html'

def shop(request):
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    context = {'mydict': mydict,}
    return render(request, 'fourth_task/sample2.html', context)

class basket(TemplateView):
    template_name = 'fourth_task/sample3.html'

# def menu(request):
#     mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
#     context = {'mydict': mydict,}
#     return render(request, 'fourth_task/sample2.html', context)