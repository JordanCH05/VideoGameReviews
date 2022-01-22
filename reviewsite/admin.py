from django.contrib import admin
from .models import Game, Review
from django_summernote.admin import SummernoteModelAdmin

# Game Content
@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status',)
    list_display = ('title', 'slug', 'score')
    search_fields = ['title', 'description']
    summernote_fields = ('description')
    actions = ['publish_games']

    def publish_games(self, request, queryset):
        queryset.update(status=1)

# Review Content
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_filter = ('approved',)
    list_display = ('username', 'game', 'score', 'created_on', 'approved')
    search_fields = ['username', 'game', 'body']
    summernote_fields = ('body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)