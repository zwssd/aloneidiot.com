#_*_coding:utf8_*_
from django.shortcuts import HttpResponse
from django.shortcuts import render,loader
from sites.models import Nav

# Create your views here.

def index(request):
    nav_list = Nav.objects.order_by('sort')
    template = loader.get_template('sites/base.html')
    context = {'nav_list': nav_list}
    return HttpResponse(template.render(context, request))
