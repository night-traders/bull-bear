from django.urls import path, include

from .views import about, home, watchlist
# WatchlistView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('watchlist/', watchlist, name='watchlist'),
    # path('watchlist/', WatchlistView.as_view(), name='watchlist'),
]
