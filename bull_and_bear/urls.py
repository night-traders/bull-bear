from django.urls import include, path

from .views import about, home, watchlist

# WatchlistView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('watchlist/', watchlist, name='watchlist'),
]
