from django.shortcuts import render
from rest_framework import mixins

from rest_framework import viewsets
from apps.endpoints.models import Endpoint
from apps.endpoints.serializers import EndpointSerializer

from apps.endpoints.models import MLAlgorithm
from apps.endpoints.serializers import MLAlgorithmSerializer

from apps.endpoints.models import MLAlgorithmStatus
from apps.endpoints.serializers import MLAlgorithmStatusSerializer

from apps.endpoints.models import MLRequest
from apps.endpoints.serializers import MLRequestSerializer

class EndpointViewset(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class= EndpointSerializer
    queryset= Endpoint.objects,all()
    
class MLAlgorithmStatusViewset(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class= MLAlgorithmStatusSerializer
    queryset= MLAlgorithmStatus.objects,all()
    
    def deactivate_other_statuses(instances):
        old_statuses= MLAlgorithmStatus.objects.filter(parent_mlalgorithm= instance.parent_mlalgortihm, created_at_lt= instance.created_at)
        for i in range(len(old_statuses)):
            old_statuses[i].active= False
            MLAlgorithmStatus.object.bulk_update(old_statuses, ["active"])
            
class MLAlgorithmViewset(mixins.RetrieveModelMixin, mixins.ListModelMixin, 
                          viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class= MLAlgorithmStatusSerializer
    queryset= MLAlgorithmStatus.objects.all()
    
    def create_perform(self, serializer):
        try:
            with translation.atomic():
                instance= serializer.save(active= True)
                #deactivate the other statuses
                deactivate_other_statuses(instance)
            
        except Exception as e:
            raise APIException(str(e))
        
class MLRequestViewset(mixins.RetrieveModelMixin, mixins.ListModelMixin, 
                          viewsets.GenericViewSet, mixins.UpdateModelMixin):
    serializer_class= MLRequestSerializer
    queryset=MLRequest.objects.all()