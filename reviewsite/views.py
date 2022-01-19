from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Game
from .forms import ReviewForm

class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.filter(approved=True).order_by('-score')
    template_name = 'index.html'
    paginate_by = 9

class GameDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(approved=True)
        game = get_object_or_404(queryset, slug=slug)
        reviews = game.reviews.filter(approved=True).order_by('created_on')

        return render(
            request,
            "game_detail.html",
            {
                "game": game,
                "reviews": reviews,
                "reviewed": False,
                "review_form": ReviewForm(),
            }
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(approved=True)
        game = get_object_or_404(queryset, slug=slug)
        reviews = game.reviews.filter(approved=True).order_by('created_on')

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.username = request.user
            review = review_form.save(commit=False)
            review.game = game
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "game_detail.html",
            {
                "game": game,
                "reviews": reviews,
                "reviewed": True,
                "review_form": ReviewForm(),
            }
        )