from django.contrib import admin
from badminton.models import Minton

class MintonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'telephone']
    list_display_links = ['name']

admin.site.register(Minton, MintonAdmin)

