#_*_coding:utf8_*_
from django.shortcuts import render
from aicms.models import Articles,Nav
from django.conf import settings

# Create your views here.

def index(request):
    nav_list = Nav.objects.order_by('sort')
    artice_list = Articles.objects.all()
    template = 'aicms/index.html'
    context = {'nav_list': nav_list, 'article_list': artice_list, 'sites_title':settings.SITES_TITLE}
    return render(request, template, context)
