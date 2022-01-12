from . import views
from django.urls import path


urlpatterns = [
    path('', views.GameList.as_view(), name='home')
]