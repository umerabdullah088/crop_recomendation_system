from datetime import timedelta
from dateutil.relativedelta import relativedelta

from crop_cycle.models import FertilizerApplication


def calculate_application_date(planting_date, schedule_item):
    if schedule_item.get("days_after_planting") is not None:
        return planting_date + timedelta(
            days=schedule_item["days_after_planting"]
        )

    if schedule_item.get("weeks_after_planting") is not None:
        return planting_date + timedelta(
            weeks=schedule_item["weeks_after_planting"]
        )

    if schedule_item.get("months_after_planting") is not None:
        return planting_date + relativedelta(
            months=schedule_item["months_after_planting"]
        )

    return None


def generate_fertilizer_applications(crop_cycle, schedule):
    applications = []

    for item in schedule:

        recommended_date = calculate_application_date(
            crop_cycle.planting_date,
            item
        )

        stage = item.get("stage", "General")

        recommendation = item.get(
            "recommendation",
            "Fertilizer application"
        )

        nutrients = item.get("nutrients", [])

        notes = item.get("notes", "")

        full_notes = f"Stage: {stage}. {recommendation}"

        if nutrients:
            full_notes += f" Nutrients: {', '.join(nutrients)}."

        if notes:
            full_notes += f" {notes}"

        application = FertilizerApplication.objects.create(
            crop_cycle=crop_cycle,
            fertilizer="",
            stage=stage,
            nutrients=", ".join(nutrients),
            recommended_date=recommended_date,
            status="PENDING",
            notes=full_notes,
        )

        applications.append(application)

    return applications