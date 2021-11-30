from django.contrib import admin
from mintonplace.models import mintongym

class mintongymAdmin(admin.ModelAdmin):
    list_display = ["place_name", "address", "parking"]
    search_fields = ['place_name']

admin.site.register(mintongym, mintongymAdmin)