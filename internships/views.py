from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Internship
from .serializers import InternshipSerializer
from users.models import CustomUser

# STUDENT VIEWS

@api_view(['POST'])
def add_internship(request):
    serializer = InternshipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_student_internships(request, student_id):
    try:
        student = CustomUser.objects.get(id=student_id, role='student')
        internships = Internship.objects.filter(student=student)
        serializer = InternshipSerializer(internships, many=True)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_internship_details(request, internship_id):
    try:
        internship = Internship.objects.get(id=internship_id)
        serializer = InternshipSerializer(internship)
        return Response(serializer.data)
    except Internship.DoesNotExist:
        return Response({'error': 'Internship not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'PATCH'])
def edit_internship(request, internship_id):
    try:
        internship = Internship.objects.get(id=internship_id)
    except Internship.DoesNotExist:
        return Response({'error': 'Internship not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = InternshipSerializer(internship, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
