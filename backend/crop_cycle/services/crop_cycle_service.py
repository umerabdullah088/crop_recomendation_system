from crop_cycle.models import CropCycle
from crop_cycle.services.schedule_service import (
    generate_fertilizer_applications,
)
from ml.schedules.fertilizer_schedules import get_schedule


def create_crop_cycle(
    crop,
    planting_date,
    expected_harvest_date=None,
    recommended_fertilizer=None,
):
    """
    Create a CropCycle and automatically generate
    its predefined fertilizer applications.
    """

    crop = crop.strip().lower()

    schedule = get_schedule(crop)

    crop_cycle = CropCycle.objects.create(
        crop=crop,
        planting_date=planting_date,
        expected_harvest_date=expected_harvest_date,
    )

    applications = generate_fertilizer_applications(
        crop_cycle,
        schedule,
    )

    # Attach the ML-recommended fertilizer to the
    # generated applications when available.
    

    return crop_cycle, applications