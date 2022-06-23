from django.views.generic import ListView
from django.shortcuts import render
import random
from django.views.generic import View

from render_test.models import SampleModel
# Create your views here.

def first_page(request):
    return render(request, 'first_page.html', {})
    
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