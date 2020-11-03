from django.urls import path, include

from .views import about, home, WatchlistView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('watchlist/', WatchlistView.as_view(), name='watchlist'),
]
