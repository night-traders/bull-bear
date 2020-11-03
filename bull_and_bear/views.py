from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Stock_ID


def home(request):

    context = {
        'title': 'Home',
    }

    return render(request, 'bull_and_bear/home.html', context)


def about(request):

    context = {
        'title': 'About'
    }

    return render(request, 'bull_and_bear/about.html', context)


class WatchlistView(ListView):
    template_name = 'bull_and_bear/watchlist.html'
    model = Stock_ID

# def watchlist(request):

#     context = {
#         'title': 'Watchlist'
#     }

#     my_stocks = Stock_ID.objects.get

#     return render(request, 'bull_and_bear/watchlist.html', context)
