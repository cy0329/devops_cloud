from django.contrib import admin

from mintonplace.models import Post, Review, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'telephone']
    list_display_links = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass