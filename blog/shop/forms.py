from django import forms

from shop.models import STATUS_CHOICES, ORDER_BY_CHOICES

class ProductFiltersForm(forms.Form):
    price__gt = forms.IntegerField(
        min_value=0,
        label="Price Min",
        widget=forms.TextInput(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )
    price__lt = forms.IntegerField(
        min_value=0,
        label="Price Max",
        widget=forms.TextInput(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )
    order_by = forms.ChoiceField(
        choices=ORDER_BY_CHOICES,
        widget=forms.Select(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )
