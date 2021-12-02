from django.contrib import admin
from CYtube.models import Cyvlog

class CyvlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cyvlog, CyvlogAdmin)