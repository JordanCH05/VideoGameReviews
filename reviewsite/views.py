from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Game

class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.filter(approved=True).order_by('-score')
    template_name = 'index.html'
    paginate_by = 9

class GameDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        reviews = game.reviews.filter(approved=True)