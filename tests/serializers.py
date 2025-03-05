from rest_framework import serializers
from users.models import CustomUser  
from .models import Test, TestResult

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__' 

class TestResultSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(source='student.username')  # Use username instead of ID
    test_name = serializers.CharField(source='test.name', read_only=True)
    percentage = serializers.FloatField(read_only=True)
    status = serializers.CharField(read_only=True)
    rank = serializers.IntegerField(read_only=True)

    class Meta:
        model = TestResult
        fields = ['id', 'student_username', 'test', 'test_name', 'score', 'percentage', 'status', 'rank']

    def create(self, validated_data):
        student_username = validated_data.pop('student')['username']  # Extract username
        try:
            student = CustomUser.objects.get(username=student_username, role='student')  # Fetch user by username
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({'student_username': 'Student not found'})

        test = validated_data['test']
        score = validated_data['score']

        # Calculate percentage
        percentage = (score / test.total_marks) * 100
        status = "Pass" if percentage >= 40 else "Fail"

        # Save the new test result
        test_result = TestResult.objects.create(
            student=student,
            test=test,
            score=score,
            percentage=percentage,
            status=status
        )

        # Recalculate Ranks for All Students in the Test
        test_results = TestResult.objects.filter(test=test).order_by('-score')  # Higher score = better rank
        rank = 1
        for result in test_results:
            result.rank = rank
            result.save()
            rank += 1

        return test_result
