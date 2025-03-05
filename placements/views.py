from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Placement
from .serializers import PlacementSerializer

from users.models import CustomUser

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
    
@api_view(['GET'])
def get_placements_by_course(request, course):
    students = CustomUser.objects.filter(course_pursuing=course)
    placements = Placement.objects.filter(student__in=students)
    
    if not placements.exists():
        return Response({'error': 'No placements found for this course'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PlacementSerializer(placements, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_placements_by_student(request, username):
    try:
        student = CustomUser.objects.get(username=username, role='student')
        placements = Placement.objects.filter(student=student)
        
        if not placements.exists():
            return Response({'error': 'No placements found for this student'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlacementSerializer(placements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_placements_by_company(request, company):
    placements = Placement.objects.filter(company__iexact=company)
    
    if not placements.exists():
        return Response({'error': 'No placements found for this company'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PlacementSerializer(placements, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def edit_placement(request, id):
    try:
        placement = Placement.objects.get(id=id)
    except Placement.DoesNotExist:
        return Response({'error': 'Placement not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PlacementSerializer(placement, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_placement(request, id):
    try:
        placement = Placement.objects.get(id=id)
    except Placement.DoesNotExist:
        return Response({'error': 'Placement not found'}, status=status.HTTP_404_NOT_FOUND)

    placement.delete()
    return Response({'message': 'Placement deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
