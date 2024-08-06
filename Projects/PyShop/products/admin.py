from django.contrib import admin
from .models import Product, Offer

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("artist", "title", "price", "stock")


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "description", "discount")


admin.site.register(Product, ProductAdmin) # we want to manage products in the admin panel

admin.site.register(Offer, OfferAdmin) # we want to manage offers in the admin panel
