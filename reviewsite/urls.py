from . import views
from django.urls import path


urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('<slug:slug>/', views.GameDetail.as_view(), name='game_detail'),
    path('edit_review/<review_id>/<slug>', views.edit_review, name='edit_review'),
    path('delete_review/<review_id>/<slug>', views.delete_review, name='delete_review'),
]