from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def main(request):
    template = loader.get_template('members_main.html')
    all_members = Member.objects.all().values().order_by('lastname', 'firstname')
    context = {
        'all_members': all_members,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    template = loader.get_template('members_details.html')
    member = Member.objects.get(id=id)
    context = {
        'member': member
    }
    return HttpResponse(template.render(context, request))
