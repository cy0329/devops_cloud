from django.contrib import admin

from shop.models import Shop, Review, Tag


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'telephone']
    list_display_links = ['name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

