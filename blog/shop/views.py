from django.db.models import F, Sum
from django.shortcuts import render
from django.core.paginator import Paginator

from shop.forms import ProductFiltersForm
from shop.models import Product


def products_view(request):
    products = Product.objects.all()
    filters_form = ProductFiltersForm(request.GET)

    if filters_form.is_valid():
        if filters_form.cleaned_data["status"]:
            products = products.filter(status=filters_form.cleaned_data["status"])
        if filters_form.cleaned_data["price__gt"]:
            products = products.filter(price__gt=filters_form.cleaned_data["price__gt"])
        if filters_form.cleaned_data["price__lt"]:
            products = products.filter(price__lt=filters_form.cleaned_data["price__lt"])

        if filters_form.cleaned_data["order_by"]:
            order_by = filters_form.cleaned_data["order_by"]
            if order_by == "price_asc":
                products = products.order_by("price")
            if order_by == "price_desc":
                products = products.order_by("-price")
            if order_by == "max_count":
                products = products.annotate(
                    total_count=Sum("purchases__count")
                ).order_by("-total_count")
            if order_by == "max_price":
                products = products.annotate(
                    total_price=Sum("purchases__count") * F("price")
                ).order_by("-total_price")

    paginator = Paginator(products, 3)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    return render(
        request,
        "products/list.html",
        {"filters_form": filters_form, "products": products},
    )
