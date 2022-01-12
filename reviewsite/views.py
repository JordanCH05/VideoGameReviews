from django.shortcuts import render
from django.views import generic
from .models import Game

class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.filter(approved=True).order_by('-score')
    template_name = 'index.html'
    paginate_by = 9
