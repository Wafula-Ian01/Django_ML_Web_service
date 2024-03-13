from rest_framework import serializers
from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints.models import MLAlgorithmStatus
from apps.endpoints.models import MLRequest

class EndpointSerializer(serializers.modelSerializers):
    class Meta:
        model= Endpoint
        read_only_fields= ("id", "name", "owner", "created_at")
        fields= read_only_fields
        
class MLAlgorithmSerializer(serializers.ModelSerializer):
    current_status= serializers.SerializerMethodField(read_only= True)
    
    def get_current_status(self, mlalgorithm):
        return MLAlgorithmStatus.object.filter(parent_algorithm= mlalgorithm).latest("created_at").status
    
    class Meta:
        model= MLAlgorithm
        read_only_fields=("id", "name", "description", 
                          "code", "version", "owner", 
                          "created_at", "parent_endpoint", "current_status")
        fields= read_only_fields
        
    class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
        class Meta:
            model= MLAlgorithmStatus
            read_only_fields= ("id", "active", "status", "created_at", 
                               "created_by", "parent_mlalgorithm")
            fields= read_only_fields
            
    class MLRequestSerializer(serializers.ModelSerializer):
        class Meta:
            model= MLRequest
            read_only_fields= ("id", "input_data", "full_response", "response", 
                               "created_at", "mlalgorithm")
            fields= ("id", "input_data", "full_response", "response", "feedback", 
                     "created_at", "mlalgorithm")