from django.shortcuts import render
#from templates.second_task import *

# Create your views here.
def render_class(request):
    return render(request, 'second_task/class_template.html')

def render_func(request):
    return render(request, 'second_task/func_template.html')