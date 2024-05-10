from django.contrib import admin
from .models import User, HouseNumbers, AllStreets, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_joined']
    search_fields = ['username']


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(HouseNumbers)
admin.site.register(AllStreets)
