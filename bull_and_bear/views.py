import os

import requests
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView

NEWS_API_KEY = os.environ['API_NEWS']
from .forms import SearchStockForm
from .models import Stock_ID

from .prediction import MakePrediction


def home(request):
    response = requests.get(f"https://stocknewsapi.com/api/v1/category?section=general&items=50&token={NEWS_API_KEY}")
    news_data = response.json()
    context = {
        'data': news_data['data']
    }
    paginator = Paginator(context['data'], 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bull_and_bear/home.html', {'page_obj': page_obj})


def about(request):

    context = {
        'title': 'About'
    }

    return render(request, 'bull_and_bear/about.html', context)


# class WatchlistView(ListView):
#     template_name = 'bull_and_bear/watchlist.html'
#     model = Stock_ID

@login_required
def watchlist(request):

    if request.method == 'POST':
        form = SearchStockForm(request.POST)

    
        if form.is_valid():
            user = request.user
            stock_ticker = request.POST.get('stock_ticker')
            company_name = request.POST.get('company_name')

            new_stock = Stock_ID(
                user=user,
                stock_ticker=stock_ticker,
                company_name=company_name,
            )
            new_stock.save()
                
            return redirect('watchlist')

    else:
        form = SearchStockForm()

    my_stocks = Stock_ID.objects.all()

    # ! right now it running a prediction on ALL stocks saved in db
    for stock in my_stocks:
        ticker = str(stock.stock_ticker)
        predictor = MakePrediction(ticker)
        stock.prediction = predictor.get_df_img()

    context = {
        'title': 'Watchlist',
        'form': form,
        'stocks': my_stocks,
    }

    return render(request, 'bull_and_bear/watchlist.html', context)

# def results(request):

#     stocks = Stock_ID.objects.get.all()
#     context = {
#         'title',: ''
#     }
