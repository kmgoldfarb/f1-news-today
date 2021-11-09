from django.shortcuts import render
from django.db.models import Q
from .models import Article
from .scrapers import get_autosport, get_wtf1

# articles = [
#    {'id': 1, 'title': 'Verstappen Wins Mexico'},
#    {'id': 2, 'title': 'Bottas Leaves Too Much Room'},
#    {'id': 3, 'title': 'Perez Scores Home Podium'},
# ] 


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    articles = Article.objects.filter(
        Q(site__icontains=q) |
        Q(title__icontains=q))
    sorted_articles = articles.order_by('-date')
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
    # get_autosport()
    return render(request, 'base/standings.html')

def upcoming(request):
    # get_wtf1()
    return render(request, 'base/upcoming.html')
