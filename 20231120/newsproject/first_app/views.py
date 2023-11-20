from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Article

# Create your views here.

def index(request):
    template = loader.get_template("first_app/index.html")
    articles = Article.objects.order_by("-created_at")[:5]
    content = {
        "articles":articles,
    }
    return HttpResponse(template.render(content,request))

def article(request,article_id):
    article = Article.objects.get(pk=article_id)
    template = loader.get_template("first_app/article.html")
    context = {
        "article":article,
    }
    return HttpResponse(template.render(context,request))
