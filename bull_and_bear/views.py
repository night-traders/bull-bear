from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render


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