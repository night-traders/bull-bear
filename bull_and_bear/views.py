import os
from datetime import date
import finnhub
import requests
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import SearchStockForm
from .models import Stock_ID, Saved_Predictions
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

            
            context = {
                'ticker': api_response['ticker'],
                'company_name': api_response['name'],
            }

            # where new stocks added to DB
            new_stock = Stock_ID(
                user=user,
                stock_ticker=context['ticker'],
                company_name=context['company_name'],
            )
            new_stock.save()

            
            return redirect('watchlist')

    else:
        form = SearchStockForm()

    my_stocks = Stock_ID.objects.all().filter(user=request.user)

    if my_stocks:
        for stock in my_stocks:
            prediction = Saved_Predictions.objects.all().filter(stock_ticker=stock.stock_ticker)

            if not prediction:
                ticker = str(stock.stock_ticker)
                predictor = MakePrediction(ticker)
                df = predictor.get_df_img()
                stock.prediction = df
                new_prediction = Saved_Predictions(
                    stock_ticker = ticker,
                    date_predicted = date.today(),
                    img = df
                )
                new_prediction.save()

            else:
                if prediction[0].date_predicted == date.today():
                    stock.prediction = prediction[0].img
                else:
                    Saved_Predictions.objects.filter(stock_ticker=stock.stock_ticker).delete()
                    ticker = str(stock.stock_ticker)
                    predictor = MakePrediction(ticker)
                    df = predictor.get_df_img()
                    stock.prediction = df
                    new_prediction = Saved_Predictions(
                        stock_ticker = ticker,
                        date_predicted = date.today(),
                        img = df
                    )
                    new_prediction.save()

    temp = date.today()

    context = {
        'title': 'Watchlist',
        'form': form,
        'stocks': my_stocks,
        'today': temp,
    }

    return render(request, 'bull_and_bear/watchlist.html', context)


