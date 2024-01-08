from django.contrib import admin
from .models import Category, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_created']
    search_fields = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
