from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "mail"]
    list_per_page = 10
    search_fields = ["name"]
