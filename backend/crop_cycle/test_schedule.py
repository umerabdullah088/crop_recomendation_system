from datetime import date

from models import CropCycle
from services.schedule_service import generate_fertilizer_applications

from ml.schedules.fertilizer_schedules import get_schedule


# Create a test crop cycle
crop_cycle = CropCycle.objects.create(
    crop="rice",
    planting_date=date(2026, 9, 20),
    expected_harvest_date=date(2027, 1, 20),
)

# Get the predefined schedule
schedule = get_schedule(crop_cycle.crop)

# Generate fertilizer applications
applications = generate_fertilizer_applications(
    crop_cycle,
    schedule
)

print("=" * 60)
print("CROP CYCLE CREATED")
print("=" * 60)

print("Crop:", crop_cycle.crop)
print("Planting Date:", crop_cycle.planting_date)

print("\nFERTILIZER APPLICATIONS")
print("=" * 60)

for application in applications:
    print("\nStage information:")
    print(application.notes)
    print("Recommended Date:", application.recommended_date)
    print("Status:", application.status)

print("=" * 60)