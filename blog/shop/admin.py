from django.contrib import admin
from shop.models import Product, Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "cost", "image", "status")
    search_fields = ("title",)


@admin.register(Purchase)
class PurshaseAdmin(admin.ModelAdmin):
    list_display = ("product", "count",)
    search_fields = ("product",)

