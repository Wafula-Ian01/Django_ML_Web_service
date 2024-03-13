from django.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewset
from apps.endpoints.views import MLAlgorithmViewset
from apps.endpoints.views import MLAlgorithmStatusViewset
from apps.endpoints.views import MLRequestViewset

router= DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewset, basename="endpoints")
router.register(r"mlalgorithm", MLAlgorithmViewset, basename="mlalgorithm")
router.register(r"mlalgorithstatuses", MLAlgorithmStatusViewset, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewset, basename="mlrequests")

urlpatterns=[
   url(r"^api/v1/", include(router.urls)),
]