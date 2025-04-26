from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import ClientViewSet, ProgramViewSet

# Schema view setup for API documentation
# This creates interactive Swagger and static Redoc documentation for the API.

schema_view = get_schema_view(
    openapi.Info(
        title="Cema Health System API",  # API title
        default_version='v1',  # Default version
        description="API documentation for managing health programs and clients",  # API description
        terms_of_service="https://www.google.com/policies/terms/",  # Link to terms of service
        contact=openapi.Contact(email="contact@cemahealth.com"),  # Contact email for the API
        license=openapi.License(name="MIT License"),  # License type
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Allows access to the documentation
)

router = DefaultRouter()  # Create a router for handling URL routing
router.register(r'clients', ClientViewSet)  # Register the ClientViewSet
router.register(r'programs', ProgramViewSet)  # Register the ProgramViewSet

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI documentation
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc UI documentation
    path('', include(router.urls)),  # Include the URLs from the router
]
