from page1.models import score
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
import datetime
from django.core import serializers


def saveScore(score1):
    time1 = datetime.datetime.now().strftime('%Y-%m-%d')
    data = score(score=score1, date=str(time1))
    data.save()


def getScore():
    es = score.objects.all().order_by('-id')
    return es


def getAllScore(request):
    ajax_testvalue = serializers.serialize("json", getScore())
    return HttpResponse(str(ajax_testvalue))

