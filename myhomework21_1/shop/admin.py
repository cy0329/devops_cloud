from django.contrib import admin

from shop.forms import ShopForm
from shop.models import Shop, Tag, Category


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    form = ShopForm
    list_display = ['id', 'name', 'address', 'telephone']
    list_display_links = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

