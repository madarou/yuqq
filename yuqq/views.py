#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from mysite import settings
# Create your views here.
def index(request):
    return render_to_response('public/index.html',{'title':'鱼圈圈'})

def aboutme(request):
    return render_to_response('public/aboutme.html',{'info':'我们是鱼圈圈'})

def services(request):
    return render_to_response('public/services.html',{'services':'洗鱼缸'})

def message(request):
    return render_to_response('public/message.html',{'message':'留言'})

def products(request):
    return render_to_response('public/products.html',{'products':'热销商品'})

def knowledge(request):
    return render_to_response('public/knowledge.html',{'knowledge':'专业知识'})

def share(request):
    return render_to_response('public/share.html',{'share':'分享'})