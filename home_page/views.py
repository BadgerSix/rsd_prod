from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import App

# Create your views here.
def main(request):
    apps_list = App.objects.all().values().order_by('name')
    template = loader.get_template('main.html')
    context = {
        'apps_list': apps_list,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    template = loader.get_template('testing.html')
    return HttpResponse(template.render())