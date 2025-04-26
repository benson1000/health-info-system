from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from .views import ClientViewSet, ProgramViewSet

# Schema view setup for API documentation
# This creates interactive Swagger and static Redoc documentation for the API.


router = DefaultRouter()  # Create a router for handling URL routing
router.register(r'clients', ClientViewSet)  # Register the ClientViewSet
router.register(r'programs', ProgramViewSet)  # Register the ProgramViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include the URLs from the router
]
