from django.db import models

class Endpoint(models.Model):
    '''
    The Endpoint object represents the ML API Endpoint
    
    Attributes:
        name: API name to be used in the URL
        owner: Owner name
        created_at: creation date of the endpoint
    '''
    
    name= models.CharField(max_length=128)
    owner= models.CharField(max_length=128)
    created_at= models.DateTimeField(auto_now_add= True, blank= True)
    
class MLAlgorithm(models.Model):
    '''
    The MLAlgorithm represents the ML algorithm object
    
    Attributes:
        name: Name of the Algorithm
        description: Description on how the algorithm works
        code: Algorithm code
        version:Algorithm versioning similar to software versioning
        owner: Owner's name
        created_at: Addition date of the MLAlgorithm
        parent_endpoint: The referencet to the endpoint
    '''
    name=models.CharField(max_length=128)
    description=models.CharField(max_length=128)
    code=models.CharField(max_length=50000)
    version=models.CharField(max_length=128)
    owner=models.CharField(max_length=128)
    created_at=models.DateTimeField(auto_now_date=True, blank= True)
    parent_endpoint=models.ForeignKey(Endpoint, on_delete= models.CASCADE)
    
class MLAlgorithmStatus(models.Model):
    '''
    MLAlgorithmStatus represents the MLAlgorithm which varies from time to time
    
    Attributes:
        status:Algorithm status in the endpoint. Possible states: testing, staging, production, ab_testing
        active: The boolean flag which points to the currently active status
        created_by: creator's name
        created_at: creation date of the status
        parent_mlalgorithm: The refence to the corresponding MLAlgorithm
    '''
    
    status= models.CharField(max_length=128)
    active= models.BooleanField()
    created_by=models. CharField(max_length=128)
    created_at= models.DateTimeField(auto_now_add=True, blank= True)
    parent_mlalgorithm= models.ForeignKey(MLAlgorithm, on_delete= models.CASCADE, related_name="status")

class MLRequest(models.Model):
    '''
        The MLRequest keeps all request information to the MLAlgorithm
        
        Attributes:
            input_data:The input data to the MLAlgorithm in JSON format
            full_response: Response of MLAlgorithm
            response: Response of ML algorithm in JSON format
            feedback: Feedback about response in JSON format
            created_at: Request creation date
            parent_mlalgorithm: Reference to MLAlgorithm used to compute response
    '''
    
    input_data= models.CharField(max_length=10000)
    full_response= models.CharField(max_length=10000)
    response= models.CharField(max_length=10000)
    feedback= models.CharField(max_length=10000, blank= True, null= True)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm= models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE,)