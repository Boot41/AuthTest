from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, ApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('employers/<int:employer_id>/', include(router.urls)),
    path('jobs/<int:job_id>/applications/', ApplicationViewSet.as_view({'get': 'list'}), name='application-list'),
    path('applications/<int:application_id>/', ApplicationViewSet.as_view({'patch': 'partial_update'}), name='application-update'),
]