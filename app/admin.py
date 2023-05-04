from django.contrib import admin

from .models import Treatment, MonthlyOffer


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "price")
    list_filter = ("category", "name")
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(MonthlyOffer)
class MonthlyOfferAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "active")
    list_filter = ("title", "active")
    search_fields = ["title"]
    ordering = ["title"]
