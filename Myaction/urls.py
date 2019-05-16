"""Myaction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import path
from django.conf.urls import url
from page1 import views,THinter,THdao,TCPDao, ScoreDao, UploadFile


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello$', views.hello),
    url(r'^index$', views.index),
    url(r'^login$', views.login),
    url(r'^test$', views.test),
    url(r'^charts$', views.charts),
    url(r'^addth$', THdao.addth),
    url(r'^getfirst$', THdao.getfirst),
    url(r'^testajax$', THdao.testajax),
    url(r'^getuserinfo$', THdao.getuserinfo),
    url(r'^getall$', THdao.getAll),
    url(r'^askimage', TCPDao.askimage),
    url(r'^imagescore', TCPDao.imagescore),
    url(r'^stopaction', TCPDao.stopaction),
    url(r'^getAllScore', ScoreDao.getAllScore),
    url(r'^upload', UploadFile.upload)
]
