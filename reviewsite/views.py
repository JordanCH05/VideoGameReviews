from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.db.models import Avg
from .models import Game, Review
from .forms import ReviewForm

class GameList(generic.ListView):
    """ A view showing list of all games """
    model = Game
    queryset = Game.objects.filter(approved=True).order_by('-score')
    template_name = 'index.html'
    paginate_by = 9

class GameDetail(View):
    """ A view to show individual game detail by unique url slug """
    def get(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(approved=True)
        game = get_object_or_404(queryset, slug=slug)
        reviews = game.reviews.filter(approved=True).order_by('created_on')

        # Update game score based on average review score
        game_score = reviews.all().aggregate(Avg('score'))['score__avg']
        if game_score == None:
            game_score = 0
        game.score = game_score
        game.save()

        return render(
            request,
            "game_detail.html",
            {
                "game": game,
                "reviews": reviews,
                "reviewed": False,
                "review_form": ReviewForm(),
                "game_score": game_score,
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(approved=True)
        game = get_object_or_404(queryset, slug=slug)
        reviews = game.reviews.filter(approved=True).order_by('created_on')

        # Update game score based on average review score
        game_score = reviews.all().aggregate(Avg('score'))['score__avg']
        if game_score == None:
            game_score = 0

        # Post Review
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.username = request.user
            # Create Review object without commiting
            review = review_form.save(commit=False)
            #  Assign current Game to Review
            review.game = game
            # Save Game Review
            review.save()
            game.score = game_score
            game.save()
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
                "game_score": game_score,
            }
        )


def delete_review(request, slug, review_id, *args, **kwargs):
    """ Delete a review """
    queryset = Game.objects.filter(approved=True)
    game = get_object_or_404(queryset, slug=slug)

    review = Review.objects.get(pk=review_id)
    review.delete()

    return redirect(reverse('game_detail', args=[game.slug]))

def edit_review(request, slug, review_id, *args, **kwargs):
    """ Edit a review """
    queryset = Game.objects.filter(approved=True)
    game = get_object_or_404(queryset, slug=slug)

    review = Review.objects.get(pk=review_id)
    review_form = ReviewForm(data=request.POST, instance=review)
    if review_form.is_valid():
        review_form.instance.email = request.user.email
        review_form.instance.username = request.user
        review_form.instance.approved = False
        # Create Review object without commiting
        edited_review = review_form.save(commit=False)
        #  Assign current Game to Review
        edited_review.game = game
        # Save Game Review
        edited_review.save()
        return render(
            request,
            "edit_review.html",
            {
                "reviewed": True,
                "review_form": review_form,
            }
        )
    else:
        review_form = ReviewForm(instance=review)

    return render(
            request,
            "edit_review.html",
            {
                "reviewed": False,
                "review_form": review_form,
            }
        )