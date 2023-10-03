from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from .models import Assignment

# Create your views here.
def main(request):
    template = loader.get_template('assignments_main.html')
    assignments_list = Assignment.objects.all().values().order_by('time_created')
    context = {
        'assignments_list': assignments_list,
    }
    return HttpResponse(template.render(context, request))

def add_assignment(request):
    return


def delete(request, id):
    #temp code til i come back to it
    # assignment = Assignment.objects.get(id=id)
    # assignment.delete()
    # messages.success(request, "Success! Assignment deleted.")

    # template = loader.get_template('assignments_main.html')
    # assignments_list = Assignment.objects.all().values().order_by('time_created')
    # context = {
    #     'assignments_list': assignments_list,
    # }
    # return HttpResponse(template.render(context, request))
    template = loader.get_template('construction.html')
    return HttpResponse(template.render())

def details(request, id):
    template = loader.get_template('assignment_details.html')
    assignment = Assignment.objects.get(id=id)
    context = {
        'assignment': assignment,
    }
    return HttpResponse(template.render(context, request))