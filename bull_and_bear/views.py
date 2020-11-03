from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import SearchStockForm
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

    print(my_stocks)

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