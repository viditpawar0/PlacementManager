from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Test, TestResult
from .serializers import TestSerializer, TestResultSerializer

@api_view(['POST'])
def create_test(request):
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#edit this and add user constraint
@api_view(['GET'])
def get_tests_by_course(request, course_name):
    tests = Test.objects.filter(course=course_name)
    serializer = TestSerializer(tests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_test_by_id(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
        serializer = TestSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Test.DoesNotExist:
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_test_result(request):
    serializer = TestResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

