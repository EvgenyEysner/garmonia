from django.contrib import admin

from .models import Treatment


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "price")
    list_filter = ("category", "name")
    search_fields = ["name"]
    ordering = ["name"]
