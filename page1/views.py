from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse("Hello world ! ")


def test(request):
    return render_to_response("test.html")


def index(request):
    return render_to_response("index.html")


def login(request):
    return render_to_response("login.html")


def charts(request):
    return render_to_response("charts.html")

