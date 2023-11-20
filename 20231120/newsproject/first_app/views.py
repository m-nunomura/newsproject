from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    message = "Hello, world!"
    return HttpResponse(message)

def page(request,page_id):
    message = "ページ"+str(page_id)
    return HttpResponse(message)