from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "crop-cycles/",
        include("crop_cycle.urls")
    ),
]