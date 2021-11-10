from django.shortcuts import render
from django.db.models import Q
from .models import Article, Driver
from .scrapers import get_autosport, get_wtf1, get_driver_standings


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    articles = Article.objects.filter(
        Q(site__icontains=q) |
        Q(title__icontains=q))
    sorted_articles = articles.order_by('-date')[:50]
    sites = Article.objects.order_by().values_list('site').distinct()
    formatted_sites = []
    for s in sites:
        formatted_sites.append(s[0])
    context =  {'articles': sorted_articles, 'sites': formatted_sites}
    return render(request, 'base/home.html', context)


def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'base/article.html', context)


def standings(request):
    drivers = Driver.objects.all().order_by('position')
    context = {'drivers': drivers}
    return render(request, 'base/standings.html', context)


def upcoming(request):
    # get_wtf1()
    # get_autosport()
    get_driver_standings()
    return render(request, 'base/upcoming.html')
