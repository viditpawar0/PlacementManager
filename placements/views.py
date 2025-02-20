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

@api_view(['GET'])
def get_placement_by_id(request, id):
    try:
        placement = Placement.objects.get(id=id)
        serializer = PlacementSerializer(placement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Placement.DoesNotExist:
        return Response({'error': 'Placement not found'}, status=status.HTTP_404_NOT_FOUND)