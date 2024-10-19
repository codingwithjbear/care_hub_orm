from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, HealthDataViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'healthdata', HealthDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]