from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from devices.views import DeviceViewSet
from events.views import EventViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r"devices", DeviceViewSet, basename="device")
router.register(r"events", EventViewSet, basename="event")

urlpatterns = [
    path("admin/", admin.site.urls),

    # OpenAPI/Swagger
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    # Auth
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),

    # API
    path("api/", include(router.urls)),
]
