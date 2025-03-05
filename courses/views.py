from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from users.models import CustomUser

@api_view(['POST'])
def add_course(request):
    student_username = request.data.get('student')
    try:
        student = CustomUser.objects.get(username=student_username, role='student')
    except CustomUser.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()
    data['student'] = student.id

    serializer = CourseSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_student_courses(request, username):
    try:
        student = CustomUser.objects.get(username=username, role='student')
        courses = Course.objects.filter(student=student)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_course_details(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'PATCH'])
def edit_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_courses_by_course_pursuing(request, course_pursuing):
    students = CustomUser.objects.filter(course_pursuing=course_pursuing, role='student')
    courses = Course.objects.filter(student__in=students)

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)
