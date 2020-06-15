from django.shortcuts import render
from .models import Post
# Create your views here.

def showArticles(request):
    articles = Post.objects.all()
    return render(request, 'blog/articles.html', {'articles':articles})
