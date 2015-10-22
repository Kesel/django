from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from blog.models import Article,User


def index(request):
    return render(request, 'blog/index.html')


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article': article})


def contact(request):
    user = User.objects.get(username='andriy')
    context = {
        'user': user,
    }
    return render(request, 'blog/contact.html', context)
