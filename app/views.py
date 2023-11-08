from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def silk(request):
    return HttpResponse('<marquee><h1>we are not talking about diary milk silk</h1></marquee>')
