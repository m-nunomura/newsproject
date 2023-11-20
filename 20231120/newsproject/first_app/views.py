from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def article(request):
    template = loader.get_template("first_app/article.html")
    context = {
        "title":"記事のタイトル",
        "content":"記事の本文",
    }
    return HttpResponse(template.render(context,request))
