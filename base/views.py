from django.shortcuts import render
from django.db.models import Q
from .models import Article, Constructor, Driver, Race
from .scrapers import get_autosport, get_sky_sports, get_wtf1, get_driver_standings, get_constructor_standings, get_upcoming_races


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
    teams = Constructor.objects.all().order_by('position')
    context = {'drivers': drivers, "teams": teams}
    return render(request, 'base/standings.html', context)


def upcoming(request):
    races = Race.objects.all().order_by('id')
    context = {'races': races}
    return render(request, 'base/upcoming.html', context)
