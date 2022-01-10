from django.contrib import admin
from .models import Game, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('approved',)
    list_display = ('title', 'slug', 'score', 'approved')
    search_fields = ['title', 'description']
    summernote_fields = ('description')

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_filter = ('approved', 'status')
    list_display = ('username', 'game', 'score', 'created_on', 'approved')
    search_fields = ['username', 'game', 'body']
    summernote_fields = ('body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)