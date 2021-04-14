from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(req):
    date=datetime.datetime.now()
    msg='<h1>Hello good morning'
    msg=msg+'<h1>Present server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)
    
