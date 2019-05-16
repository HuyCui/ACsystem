from django.http import HttpResponse
from django.shortcuts import render_to_response
from . import THinter
import json
from django.core import serializers
from page1.models import user

def addth(request):
    if 'temp' in request.GET and 'hmui' in request.GET:
        if THinter.addthdata(float(request.GET['temp']), float(request.GET['hmui'])):
            massage = "success"
    else:
        massage = "你提交了空表单"
    return HttpResponse(massage)


def getfirst(request):
    return HttpResponse(THinter.getadata())


def testajax(request):
    ajax_testvalue = serializers.serialize("json", THinter.getadata())
    return HttpResponse(ajax_testvalue)


def getuserinfo(request):
    flag = THinter.checkuser(request.POST['name'], request.POST['pwd'])
    #return HttpResponse(json.dumps(userobj, default=user.obj_to_json))
    if flag:
        return HttpResponse('true')
    else:
        return HttpResponse('false')


def getAll(request):
    ajax_testvalue = serializers.serialize("json", THinter.getAll())
    return HttpResponse(str(ajax_testvalue))
