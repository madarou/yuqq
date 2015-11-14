#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from mysite import settings
# Create your views here.
def index(request):
    return render_to_response('public/index.html',{'title':settings.STATIC_URL})