from django.contrib import admin
from .models import VisitorAccessRequest


class VisitorAccessRequestAdmin(admin.ModelAdmin):
    list_display = ['access_code', 'visitor_name', 'gender', 'creator']
    search_fields = ['creator']


admin.site.register(VisitorAccessRequest, VisitorAccessRequestAdmin)
