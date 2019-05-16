from django.http import HttpResponse
from page1.models import thdata, user


def addthdata(temp, hmui):
    data = thdata(temp=temp, hmui=hmui)
    data.save()
    return True


def getadata():
    es = thdata.objects.all().order_by('-id')[:1]
    return es


def checkuser(name, pwd):
    rst = user.objects.get(username='admin')
    jsonobj = user.obj_to_json(rst)
    if jsonobj['password'] == pwd:
        return True
    else:
        return False


def getAll():
    es = thdata.objects.all().order_by('-id')
    return es

