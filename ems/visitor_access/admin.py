from django.contrib import admin
from .models import VisitorAccessRequest


class VisitorAccessRequestAdmin(admin.ModelAdmin):
    list_display = ['request_number', 'visitor_name', 'gender', 'creator']
    search_fields = ['creator']


admin.site.register(VisitorAccessRequest, VisitorAccessRequestAdmin)
