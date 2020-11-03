from crispy_forms.layout import Field
from django import forms
from .models import Stock_ID


class SearchStockForm(forms.ModelForm):

    class Meta:
        model = Stock_ID
        fields = ['stock_ticker']



