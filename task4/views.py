from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class based(TemplateView):
    template_name = 'sample1.html'

#class shop(TemplateView):
#    template_name = 'sample2.html'

class basket(TemplateView):
    template_name = 'sample3.html'

def menu(request):
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    context = {'mydict': mydict,}
    return render(request, 'sample2.html', context)