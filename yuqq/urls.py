#!/usr/bin/env python
# coding: utf-8
'''
Created on 2015年11月12日

@author: makao
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]