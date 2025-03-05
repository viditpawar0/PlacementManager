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
        print("hello")
        test = Test.objects.get(id=test_id)
        print(f"Found Test: {test}")  # Debug print
        serializer = TestSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Test.DoesNotExist:
        print(f"Test with ID {test_id} not found!")  # Debug print
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_test_result(request):
    serializer = TestResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_test(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
        serializer = TestSerializer(test, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Test.DoesNotExist:
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_test(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
        test.delete()
        return Response({"message": "Test deleted successfully"}, status=status.HTTP_200_OK)
    except Test.DoesNotExist:
        return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_results_by_student(request, username):
    try:
        results = TestResult.objects.filter(student__username=username)
        serializer = TestResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except TestResult.DoesNotExist:
        return Response({"error": "No results found for this student"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_results_by_test(request, test_id):
    results = TestResult.objects.filter(test_id=test_id).order_by('-score')
    serializer = TestResultSerializer(results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def edit_test_result(request, result_id):
    try:
        result = TestResult.objects.get(id=result_id)
        serializer = TestResultSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except TestResult.DoesNotExist:
        return Response({"error": "Test result not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_top_performers(request, test_id):
    results = TestResult.objects.filter(test_id=test_id).order_by('-score')[:5]
    serializer = TestResultSerializer(results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
