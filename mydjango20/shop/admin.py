from django.contrib import admin

from shop.forms import ShopForm
from shop.models import Shop, Review, Tag, Category


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    form = ShopForm
    list_display = ['id', 'name', 'telephone']
    list_display_links = ['name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

