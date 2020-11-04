from django.urls import include, path

from .views import about, delete_stock, home, watchlist

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('watchlist/', watchlist, name='watchlist'),
    path('delete_stock/<int:stock_id>/', delete_stock, name='delete_stock'),
]
