from django.db.models import F, Sum
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages

from shop.forms import ProductFiltersForm, PurchasesFiltersForm
from shop.models import Product, Purchase


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


def product_details_view(request, *args, **kwargs):
    product = Product.objects.get(id=kwargs["product_id"])

    # Add PRODUCTS to favorites
    if request.user.is_authenticated and request.method == "POST":
        if request.POST["action"] == "add":
            product.favorites.add(request.user)
            messages.info(request, "Product successfully added to favorites")
        elif request.POST["action"] == "remove":
            product.favorites.remove(request.user)
            messages.info(request, "Product successfully removed to favorites")
        elif request.POST["action"] == "purchase":
            Purchase.objects.create(product=product, user=request.user, count=int(request.POST["count"]))
            messages.info(request, "Product successfully purchased!")
        redirect("product_details_view", product_id=product.id)

class PurchaseView(TemplateView):
    template_name = "products/purchases.html"

    def get_context_data(self, **kwargs):
        if not self.request.user.is_authenticated:
            raise Http404
        purchases = Purchase.objects.filter(user=self.request.user)
        filters_form = PurchasesFiltersForm(self.request.GET)
        if filters_form.is_valid() and filters_form.cleaned_data["order_by"]:
            purchases = purchases.order_by(filters_form.cleaned_data["order_by"])
        return {"purchases": purchases, "filters_form": filters_form}
