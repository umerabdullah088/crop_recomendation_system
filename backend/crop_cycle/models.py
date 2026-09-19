from django.db import models


class CropCycle(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    crop = models.CharField(max_length=100)

    planting_date = models.DateField()

    expected_harvest_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.crop} - {self.planting_date}"


class FertilizerApplication(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPLIED", "Applied"),
        ("SKIPPED", "Skipped"),
    ]

    crop_cycle = models.ForeignKey(
        CropCycle,
        on_delete=models.CASCADE,
        related_name="fertilizer_applications"
    )

    fertilizer = models.CharField(max_length=150, blank=True)

    stage = models.CharField(max_length=100, blank=True)

    nutrients = models.CharField(max_length=100, blank=True)

    recommended_date = models.DateField(null=True, blank=True)

    application_date = models.DateField(null=True, blank=True)

    quantity = models.FloatField(null=True, blank=True)

    quantity_unit = models.CharField(max_length=20, default="kg")

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop_cycle.crop} - {self.stage}"