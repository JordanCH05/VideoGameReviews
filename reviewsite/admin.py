from django.contrib import admin
from .models import Game
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Game)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
