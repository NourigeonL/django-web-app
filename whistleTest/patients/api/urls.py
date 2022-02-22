from django.urls import path, include
from patients.api.views import (
    ApiImageViewSet,
    ApiPatientViewSet,
)
from rest_framework import routers
router = routers.SimpleRouter()
# router.register(r'patient', ApiPatientViewSet)
# router.register(r'image', ApiImageDetailView)

urlpatterns = [
    path('', ApiPatientViewSet.as_view({'get': 'list'}), name='list'),
    path('<slug:slug>/',
         ApiPatientViewSet.as_view({'get': 'retrieve'}), name='details'),
    # path('<slug:slug>/', include(router.urls)),
    path('<slug:slug>/images/',
         ApiImageViewSet.as_view({'get': 'list'})),
    path('<slug:slug>/images/<int:num>',
         ApiImageViewSet.as_view({'get': 'retrieve'}), name='image-detail'),
]
urlpatterns += router.urls
