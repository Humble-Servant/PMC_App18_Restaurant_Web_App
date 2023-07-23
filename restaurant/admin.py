from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("menu_item", "status")
    list_filter = ("status", )
    search_fields = ("menu_item", "description")
    

admin.site.register(Item, MenuItemAdmin)
