from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Placement
from .serializers import PlacementSerializer

@api_view(['GET'])
def get_all_placements(request):
    users = Placement.objects.all()
    serializer = PlacementSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_placement(request):
    serializer = PlacementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)