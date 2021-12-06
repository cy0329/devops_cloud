from django.contrib import admin
from badminton.models import Minton

@admin.register(Minton)
class MintonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'telephone']
    list_display_links = ['name']

