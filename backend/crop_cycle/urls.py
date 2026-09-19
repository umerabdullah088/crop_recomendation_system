from django.urls import path

from .views import (
    create_crop_cycle_view,
    crop_cycle_list_view,
    crop_cycle_detail_view,
    update_fertilizer_application_view,
    predict_and_create_crop_cycle,
    recommend_fertilizer_view
)


urlpatterns = [
    path(
        "",
        crop_cycle_list_view,
        name="crop_cycle_list",
    ),

    path(
        "create/",
        create_crop_cycle_view,
        name="create_crop_cycle",
    ),
 path(
    "<int:cycle_id>/fertilizer/<int:application_id>/recommend/",
    recommend_fertilizer_view,
    name="recommend_fertilizer",
),
    path(
        "<int:cycle_id>/",
        crop_cycle_detail_view,
        name="crop_cycle_detail",
    ),
    path(
    "fertilizer/<int:application_id>/",
    update_fertilizer_application_view,
    name="update_fertilizer_application",
),

path(
    "predict/",
    predict_and_create_crop_cycle,
    name="predict_and_create_crop_cycle",
),

]