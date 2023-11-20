from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Article
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    model = Article
    template_name = "first_app/index.html"

    def get_queryset(self):
        return Article.objects.order_by("-created_at")[:5]
    
class ArticleView(generic.DetailView):
    model = Article
    template_name = "first_app/article.html"