"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from yuqq import views
from . import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name='index'),
    url(r'^services/$',views.services,name='services'),
    url(r'^services/(?P<kind>[a-z]+)/$',views.services,name='services'),
    url(r'^aboutme/$',views.aboutme,name='aboutme'),
    url(r'^message/$',views.message,name='message'),
    url(r'^products/$',views.products,name='products'),
    url(r'^products/(?P<catalogue>[a-z]+)/(?P<kind>[a-z]+)/$',views.products,name='products'),
    url(r'^knowledge/$',views.knowledge,name='knowledge'),
    url(r'^share/$',views.share,name='share'),
    url(r'^detail/$',views.detail,name='detail'),
    url(r'^detail/(?P<name>[\S]+)$',views.detail,name='detail'),
    url(r'^messagepost/$',views.messagepost,name='messagepost'),
    url(r'^news/$',views.news,name='news'),
    url(r'^tips/(?P<num>\d+)$',views.tips,name='tips'),
    #url(r'^img/(?P/pathpath.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
    #url(r'^public/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL } ),
]
