import os

import finnhub
import requests
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import SearchStockForm
from .models import Stock_ID
from .prediction import MakePrediction

NEWS_API_KEY = os.environ['API_NEWS']
FINNHUB = os.environ['FINNHUB']

def home(request):
    response = requests.get(f"https://stocknewsapi.com/api/v1/category?section=general&items=50&token={NEWS_API_KEY}")
    news_data = response.json()
    context = {
        'data': news_data['data']
    }
    paginator = Paginator(context['data'], 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bull_and_bear/home.html', {'page_obj': page_obj})


def about(request):

    context = {
        'title': 'About'
    }

    return render(request, 'bull_and_bear/about.html', context)


@login_required
def watchlist(request):

    if request.method == 'POST':
        form = SearchStockForm(request.POST)

    
        if form.is_valid():
            user = request.user
            stock_ticker = request.POST.get('stock_ticker')
            
            response = requests.get(f"https://finnhub.io/api/v1/stock/profile2?symbol={stock_ticker}&token={FINNHUB}")
            api_response = response.json()
            print('api response', api_response)
            
            context = {
                'ticker': api_response['ticker'],
                'company_name': api_response['name'],
            }
            print('context is', context)

            new_stock = Stock_ID(
                user=user,
                stock_ticker=context['ticker'],
                company_name=context['company_name'],
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


