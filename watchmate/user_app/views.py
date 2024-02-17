from rest_framework.decorators import api_view
from .serializers import RegisterationSerializer

@api_view(['POST',])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data