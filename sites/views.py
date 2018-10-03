#_*_coding:utf8_*_
from django.shortcuts import render
from sites.models import Articles,Nav
from django.conf import settings

# Create your views here.

def index(request):
    nav_list = Nav.objects.order_by('sort')
    template = 'sites/index.html'
    context = {'nav_list': nav_list, 'sites_title':settings.SITES_TITLE}
    return render(request, template, context)
