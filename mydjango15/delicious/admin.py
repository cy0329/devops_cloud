from django.contrib import admin
from delicious.models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'latitude', 'longitude', 'telephone']
    list_display_links = ['name'] # --> admin에서 정보 보기 위한 링크


admin.site.register(Shop, ShopAdmin)
