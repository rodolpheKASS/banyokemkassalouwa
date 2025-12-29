from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Article
from .serializers import ArticleSerializer

class ArticleListView(ListAPIView):
    queryset = Article.objects.filter(archived=False)
    serializer_class = ArticleSerializer
