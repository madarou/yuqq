#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from mysite import settings
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import datetime
import json
from .models import *
# Create your views here.
def index(request):
    index=serializers.serialize("json", Index.objects.all())
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
        ip =  request.META['HTTP_X_FORWARDED_FOR']  
    else:  
        ip = request.META['REMOTE_ADDR'] 
    visitor = Visitor(ip=ip,time=datetime.datetime.now())
    visitor.save()
    return render_to_response('public/index.html',{'Index':index})

def aboutme(request):
    return render_to_response('public/aboutme.html',{'info':'我们是鱼圈圈'})

def services(request,kind='none'):
    return render_to_response('public/services.html',{'Service':json.dumps(kind)})

def message(request):
    return render_to_response('public/message.html')

def products(request,catalogue='none', kind='none'):
    products=None
    if catalogue=='none' and kind=='none':
        products=serializers.serialize("json", Product.objects.filter(show='yes'))
    elif catalogue != 'none':
        products=serializers.serialize("json", Product.objects.filter(catalogue=catalogue,show='yes'))
    elif kind != 'none':
        products=serializers.serialize("json", Product.objects.filter(kind=kind,show='yes'))
    else:
        products=serializers.serialize("json", Product.objects.filter(show='yes'))
    return render_to_response('public/products.html',{'Products':products})

def knowledge(request):
    return render_to_response('public/knowledge.html',{'knowledge':'专业知识'})

def share(request):
    List = ['自强学堂', '渲染Json到模板']
    return render_to_response('public/share.html',{'List': json.dumps(List)})

def detail(request,name):
    intro = Introduction.objects.get(name=name).toJSON()
    '''
    all()返回的list可以用serializers.serialize序列化，但get()返回
    的单个model对象不能，只能用自定义的toJSON()方法
    '''
    #product = Product.objects.all()
    #json_data = serializers.serialize("json", product)
    product = Product.objects.get(name=name).toJSON()
    return render_to_response('public/detail.html',{'Product': product,'Introduction':intro})

@csrf_exempt
def messagepost(request):
    user_name = request.POST['user_name']
    contact = request.POST['user_contact']
    content = request.POST['user_message']
    message = Message(user_name=user_name,contact=contact,content=content,time=datetime.datetime.now())
    message.save()
    return HttpResponseRedirect('/message')