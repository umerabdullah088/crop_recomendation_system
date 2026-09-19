import json
from ml_service.crop_predictor import predict_crop
from ml_service.fertilizer_predictor import predict_fertilizer
from crop_cycle.services.crop_cycle_service import create_crop_cycle
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from crop_cycle.models import CropCycle, FertilizerApplication
from ml_service.fertilizer_predictor import predict_fertilizer

from crop_cycle.services.crop_cycle_service import create_crop_cycle
from crop_cycle.models import (
    CropCycle,
    FertilizerApplication,
)


@csrf_exempt
def create_crop_cycle_view(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed."},
            status=405
        )

    try:
        data = json.loads(request.body)

        crop = data.get("crop")
        planting_date = data.get("planting_date")
        expected_harvest_date = data.get(
            "expected_harvest_date"
        )

        if not crop or not planting_date:
            return JsonResponse(
                {
                    "error": "crop and planting_date are required."
                },
                status=400
            )

        from datetime import date

        planting_date = date.fromisoformat(planting_date)

        if expected_harvest_date:
            expected_harvest_date = date.fromisoformat(
                expected_harvest_date
            )

        crop_cycle, applications = create_crop_cycle(
            crop=crop,
            planting_date=planting_date,
            expected_harvest_date=expected_harvest_date,
        )

        return JsonResponse(
            {
                "message": "Crop cycle created successfully.",
                "crop_cycle": {
                    "id": crop_cycle.id,
                    "crop": crop_cycle.crop,
                    "planting_date": str(
                        crop_cycle.planting_date
                    ),
                    "expected_harvest_date": (
                        str(crop_cycle.expected_harvest_date)
                        if crop_cycle.expected_harvest_date
                        else None
                    ),
                    "status": crop_cycle.status,
                },
                "fertilizer_applications": [
                    {
                        "id": application.id,
                        "fertilizer": application.fertilizer,
                        "recommended_date": (
                            str(application.recommended_date)
                            if application.recommended_date
                            else None
                        ),
                        "status": application.status,
                        "notes": application.notes,
                    }
                    for application in applications
                ],
            },
            status=201
        )

    except ValueError as error:
        return JsonResponse(
            {"error": str(error)},
            status=400
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON."},
            status=400
        )

    except Exception as error:
        return JsonResponse(
            {"error": str(error)},
            status=500
        )


def crop_cycle_list_view(request):

    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed."},
            status=405
        )

    crop_cycles = CropCycle.objects.all().order_by("-created_at")

    result = []

    for crop_cycle in crop_cycles:

        applications = []

        for application in crop_cycle.fertilizer_applications.all():
          applications.append({
    "id": application.id,
    "stage": application.stage,
    "nutrients": (
        application.nutrients.split(", ")
        if application.nutrients
        else []
    ),
    "fertilizer": application.fertilizer or "Not decided yet",
    "recommended_date": (
        str(application.recommended_date)
        if application.recommended_date
        else None
    ),
    "application_date": (
        str(application.application_date)
        if application.application_date
        else None
    ),
    "status": application.status,
    "notes": application.notes,
})

        result.append({
            "id": crop_cycle.id,
            "crop": crop_cycle.crop,
            "planting_date": str(crop_cycle.planting_date),
            "expected_harvest_date": (
                str(crop_cycle.expected_harvest_date)
                if crop_cycle.expected_harvest_date
                else None
            ),
            "status": crop_cycle.status,
            "fertilizer_applications": applications,
        })

    return JsonResponse(
        {
            "count": len(result),
            "crop_cycles": result,
        }
    )


# def crop_cycle_detail_view(request, cycle_id):

    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed."},
            status=405
        )

    try:
        crop_cycle = CropCycle.objects.get(id=cycle_id)

    except CropCycle.DoesNotExist:
        return JsonResponse(
            {"error": "Crop cycle not found."},
            status=404
        )

        applications = []

    for application in crop_cycle.fertilizer_applications.all():
        applications.append({
            "id": application.id,
            "fertilizer": application.fertilizer,
            "stage": application.stage,
            "nutrients": (
                application.nutrients.split(", ")
                if application.nutrients
                else []
            ),
            "recommended_date": (
                str(application.recommended_date)
                if application.recommended_date
                else None
            ),
            "application_date": (
                str(application.application_date)
                if application.application_date
                else None
            ),
            "status": application.status,
            "notes": application.notes,
        })

    return JsonResponse({
        "id": crop_cycle.id,
        "crop": crop_cycle.crop,
        "planting_date": str(crop_cycle.planting_date),
        "expected_harvest_date": (
            str(crop_cycle.expected_harvest_date)
            if crop_cycle.expected_harvest_date
            else None
        ),
        "status": crop_cycle.status,
        "fertilizer_applications": applications,
    })
def crop_cycle_detail_view(request, cycle_id):

    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed."},
            status=405
        )

    try:
        crop_cycle = CropCycle.objects.get(id=cycle_id)

    except CropCycle.DoesNotExist:
        return JsonResponse(
            {"error": "Crop cycle not found."},
            status=404
        )

    applications = []

    for application in crop_cycle.fertilizer_applications.all():
       applications.append({
    "id": application.id,
    "stage": application.stage,
    "nutrients": (
        application.nutrients.split(", ")
        if application.nutrients
        else []
    ),
    "fertilizer": application.fertilizer or "Not decided yet",
    "recommended_date": (
        str(application.recommended_date)
        if application.recommended_date
        else None
    ),
    "application_date": (
        str(application.application_date)
        if application.application_date
        else None
    ),
    "status": application.status,
    "notes": application.notes,
})

    return JsonResponse({
        "id": crop_cycle.id,
        "crop": crop_cycle.crop,
        "planting_date": str(crop_cycle.planting_date),
        "expected_harvest_date": (
            str(crop_cycle.expected_harvest_date)
            if crop_cycle.expected_harvest_date
            else None
        ),
        "status": crop_cycle.status,
        "fertilizer_applications": applications,
    })



@csrf_exempt
def update_fertilizer_application_view(request, application_id):

    if request.method != "PATCH":
        return JsonResponse(
            {"error": "Only PATCH method is allowed."},
            status=405
        )

    try:
        from datetime import date

        application = FertilizerApplication.objects.get(
            id=application_id
        )

        data = json.loads(request.body)

        status = data.get("status")
        application_date = data.get("application_date")

        if status:
            valid_statuses = {
                choice[0]
                for choice in FertilizerApplication.STATUS_CHOICES
            }

            if status not in valid_statuses:
                return JsonResponse(
                    {
                        "error": "Invalid status.",
                        "valid_statuses": list(valid_statuses),
                    },
                    status=400
                )

            application.status = status

        if application_date:
            application.application_date = date.fromisoformat(
                application_date
            )

        application.save()

        return JsonResponse({
            "message": "Fertilizer application updated successfully.",
            "fertilizer_application": {
                "id": application.id,
                "crop_cycle_id": application.crop_cycle.id,
                "fertilizer": application.fertilizer,
                "recommended_date": (
                    str(application.recommended_date)
                    if application.recommended_date
                    else None
                ),
                "application_date": (
                    str(application.application_date)
                    if application.application_date
                    else None
                ),
                "status": application.status,
                "notes": application.notes,
            }
        })

    except FertilizerApplication.DoesNotExist:
        return JsonResponse(
            {"error": "Fertilizer application not found."},
            status=404
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON."},
            status=400
        )

    except ValueError as error:
        return JsonResponse(
            {"error": str(error)},
            status=400
        )

@csrf_exempt
def predict_and_create_crop_cycle(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed."},
            status=405
        )

    try:
        data = json.loads(request.body)

        required_fields = [
            "nitrogen",
            "phosphorus",
            "potassium",
            "temperature",
            "humidity",
            "ph",
            "rainfall",
            "moisture",
            "carbon",
            "soil",
            "planting_date",
        ]

        missing_fields = [
            field
            for field in required_fields
            if field not in data
        ]

        if missing_fields:
            return JsonResponse(
                {
                    "error": "Missing required fields.",
                    "missing_fields": missing_fields,
                },
                status=400
            )

        from datetime import date

        # -------------------------
        # 1. Crop prediction
        # -------------------------

        crop = predict_crop(
            nitrogen=data["nitrogen"],
            phosphorus=data["phosphorus"],
            potassium=data["potassium"],
            temperature=data["temperature"],
            humidity=data["humidity"],
            ph=data["ph"],
            rainfall=data["rainfall"],
        )

        # -------------------------
        # 2. Fertilizer prediction
        # -------------------------

        fertilizer = predict_fertilizer(
            temperature=data["temperature"],
            moisture=data["moisture"],
            rainfall=data["rainfall"],
            ph=data["ph"],
            nitrogen=data["nitrogen"],
            phosphorous=data["phosphorus"],
            potassium=data["potassium"],
            carbon=data["carbon"],
            soil=data["soil"],
            crop=crop,
        )

        # -------------------------
        # 3. Create CropCycle
        # -------------------------

        planting_date = date.fromisoformat(
            data["planting_date"]
        )

        expected_harvest_date = None

        if data.get("expected_harvest_date"):
            expected_harvest_date = date.fromisoformat(
                data["expected_harvest_date"]
            )

        crop_cycle, applications = create_crop_cycle(
            crop=crop,
            planting_date=planting_date,
            expected_harvest_date=expected_harvest_date,
            recommended_fertilizer=fertilizer,
        )

        return JsonResponse(
            {
                "message": "Crop and fertilizer recommendations generated successfully.",
                "prediction": {
                    "crop": crop,
                    "fertilizer": fertilizer,
                },
                "crop_cycle": {
                    "id": crop_cycle.id,
                    "crop": crop_cycle.crop,
                    "planting_date": str(
                        crop_cycle.planting_date
                    ),
                    "expected_harvest_date": (
                        str(crop_cycle.expected_harvest_date)
                        if crop_cycle.expected_harvest_date
                        else None
                    ),
                    "status": crop_cycle.status,
                },
                "fertilizer_applications": [
                    {
                        "id": application.id,
                        "fertilizer": application.fertilizer,
                        "recommended_date": (
                            str(application.recommended_date)
                            if application.recommended_date
                            else None
                        ),
                        "status": application.status,
                        "notes": application.notes,
                    }
                    for application in applications
                ],
            },
            status=201
        )

    except ValueError as error:
        return JsonResponse(
            {"error": str(error)},
            status=400
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON."},
            status=400
        )

    except Exception as error:
        return JsonResponse(
            {"error": str(error)},
            status=500
        )



@csrf_exempt
def recommend_fertilizer_view(request, cycle_id, application_id):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed."},
            status=405
        )

    try:
        crop_cycle = CropCycle.objects.get(id=cycle_id)

    except CropCycle.DoesNotExist:
        return JsonResponse(
            {"error": "Crop cycle not found."},
            status=404
        )

    try:
        application = FertilizerApplication.objects.get(
            id=application_id,
            crop_cycle=crop_cycle
        )

    except FertilizerApplication.DoesNotExist:
        return JsonResponse(
            {"error": "Fertilizer application not found for this crop cycle."},
            status=404
        )

    try:
        data = json.loads(request.body)

        required_fields = [
            "temperature",
            "moisture",
            "rainfall",
            "ph",
            "nitrogen",
            "phosphorous",
            "potassium",
            "carbon",
            "soil",
        ]

        missing_fields = [
            field for field in required_fields
            if field not in data
        ]

        if missing_fields:
            return JsonResponse(
                {
                    "error": "Missing required fields.",
                    "fields": missing_fields
                },
                status=400
            )

        fertilizer = predict_fertilizer(
            temperature=data["temperature"],
            moisture=data["moisture"],
            rainfall=data["rainfall"],
            ph=data["ph"],
            nitrogen=data["nitrogen"],
            phosphorous=data["phosphorous"],
            potassium=data["potassium"],
            carbon=data["carbon"],
            soil=data["soil"],
            crop=crop_cycle.crop,
        )

        application.fertilizer = fertilizer
        application.save()

        return JsonResponse({
            "message": "Fresh fertilizer recommendation generated successfully.",
            "crop": crop_cycle.crop,
            "stage": application.stage,
            "fertilizer": fertilizer,
            "application": {
                "id": application.id,
                "recommended_date": (
                    str(application.recommended_date)
                    if application.recommended_date
                    else None
                ),
                "status": application.status,
            }
        })

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON."},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=500
        )