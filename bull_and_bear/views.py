from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
import requests
import os
from django.core.paginator import Paginator
NEWS_API_KEY = os.environ['API_NEWS']

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