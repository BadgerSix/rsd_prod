from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import App
from .forms import TestForm

# Create your views here.
def main(request):
    apps_list = App.objects.all().values().order_by('name')
    template = loader.get_template('main.html')
    context = {
        'apps_list': apps_list,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def testing(request):
    template = loader.get_template('testing.html')

    if request.method == 'POST':
        form = TestForm(request.POST)
        # if form.is_valid():
        #     context = {
        #         'form': form,
        #     }
    else:
        form = TestForm()

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))