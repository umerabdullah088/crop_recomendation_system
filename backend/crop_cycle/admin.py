from django.contrib import admin
from .models import CropCycle, FertilizerApplication


@admin.register(CropCycle)
class CropCycleAdmin(admin.ModelAdmin):
    list_display = (
        "crop",
        "planting_date",
        "expected_harvest_date",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "crop",
    )

    search_fields = (
        "crop",
    )


@admin.register(FertilizerApplication)
class FertilizerApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "fertilizer",
        "crop_cycle",
        "recommended_date",
        "application_date",
        "status",
    )

    list_filter = (
        "status",
        "fertilizer",
    )

    search_fields = (
        "fertilizer",
        "crop_cycle__crop",
    )