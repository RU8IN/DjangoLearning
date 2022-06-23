from django.views.generic import ListView
from django.shortcuts import render
import random
from django.views.generic import View, TemplateView

from render_test.models import SampleModel
# Create your views here.

def first_page(request):
    return render(request, 'home.html', {})
    
def web_tech(request):
    var = random.randrange(-10000, 10000)
    string = ''.join([chr(i) for i in [random.randrange(65, 122) for i in range(200)]])
    return render(request, 'web_tech.html', 
    {"random": var,
    "string": string})
    

class SampleModelView(ListView):
    model = SampleModel
    context_object_name = 'samples'
    template_name='class_view_test.html'

class AiogramTesting(TemplateView):
    template_name = "aiogram_testing.html"