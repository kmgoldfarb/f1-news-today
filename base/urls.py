from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('standings/', views.standings, name="standings"),
    path('article/<str:pk>', views.article, name="article"),
    path('upcoming/', views.upcoming, name="upcoming")
]