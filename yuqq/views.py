#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from mysite import settings
from django.core import serializers
import json
from .models import *
# Create your views here.
def index(request):
    return render_to_response('public/index.html',{'title':'鱼圈圈'})

def aboutme(request):
    return render_to_response('public/aboutme.html',{'info':'我们是鱼圈圈'})

def services(request):
    return render_to_response('public/services.html',{'services':'洗鱼缸'})

def message(request):
    return render_to_response('public/message.html',{'message':'留言'})

def products(request,catalogue='none', kind='none'):
    products=None
    if catalogue=='none' and kind=='none':
        products=serializers.serialize("json", Product.objects.all())
    elif catalogue != 'none':
        products=serializers.serialize("json", Product.objects.filter(catalogue=catalogue))
    elif kind != 'none':
        products=serializers.serialize("json", Product.objects.filter(kind=kind))
    else:
        products=serializers.serialize("json", Product.objects.all())
    return render_to_response('public/products.html',{'Products':products})

def knowledge(request):
    return render_to_response('public/knowledge.html',{'knowledge':'专业知识'})

def share(request):
    List = ['自强学堂', '渲染Json到模板']
    return render_to_response('public/share.html',{'List': json.dumps(List)})

def detail(request):
    intro = Introduction.objects.get(name="血色鹦鹉").toJSON()
    '''
    all()返回的list可以用serializers.serialize序列化，但get()返回
    的单个model对象不能，只能用自定义的toJSON()方法
    '''
    #product = Product.objects.all()
    #json_data = serializers.serialize("json", product)
    product = Product.objects.get(name="血色鹦鹉").toJSON()
    return render_to_response('public/detail.html',{'Product': product,'Introduction':intro})