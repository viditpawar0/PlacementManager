from django.shortcuts import render
import os
import pickle
import numpy as np
import traceback
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import PredictionInputSerializer
from sklearn.ensemble import RandomForestClassifier  # or whatever model you're using

# Create your views here.

# Load the model when the server starts
model_path = os.path.join(settings.BASE_DIR, 'prediction', 'ml_model', 'model.pkl')
try:
    print(f"Attempting to load model from: {model_path}")
    print(f"File exists: {os.path.exists(model_path)}")
    with open(model_path, 'rb') as model_file:
        loaded_data = pickle.load(model_file)
        print(f"Loaded data type: {type(loaded_data)}")
        print(f"Loaded data content: {loaded_data}")
        
        # Create and train a simple model (you should replace this with your actual trained model)
        # This is just a placeholder model for demonstration
        model = RandomForestClassifier()
        X = np.array([
            [8.5, 2, 3, 5, 75, 4],  # Sample positive case
            [6.0, 0, 1, 2, 60, 2],  # Sample negative case
        ])
        y = np.array([1, 0])  # 1 for placed, 0 for not placed
        model.fit(X, y)
        loaded_model = model
        print("Created and trained a simple model")
        
except Exception as e:
    print(f"Error loading model: {e}")
    print(f"Traceback: {traceback.format_exc()}")
    loaded_model = None

@api_view(['POST'])
def predict_placement(request):
    if loaded_model is None:
        return Response(
            {"error": "Model not loaded. Check server logs for details."}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    print(f"Received request data: {request.data}")
    serializer = PredictionInputSerializer(data=request.data)
    
    if serializer.is_valid():
        # Extract the features in the correct order
        features = [
            float(serializer.validated_data['cgpa']),
            float(serializer.validated_data['internships']),
            float(serializer.validated_data['projects']),
            float(serializer.validated_data['technical_skills']),
            float(serializer.validated_data['aptitude_test_score']),
            float(serializer.validated_data['soft_skills'])
        ]
        
        print(f"Extracted features: {features}")
        
        try:
            sample_data = np.array([features])
            print(f"Making prediction with data: {sample_data}")
            
            predicted_class = loaded_model.predict(sample_data)[0]
            predicted_probability = loaded_model.predict_proba(sample_data)[0][1]
            
            response_data = {
                'predicted_class': int(predicted_class),
                'placement_probability': float(predicted_probability),
            }
            print(f"Prediction successful: {response_data}")
            return Response(response_data)
            
        except Exception as e:
            error_msg = f"Prediction error: {str(e)}\nTraceback: {traceback.format_exc()}"
            print(error_msg)
            return Response(
                {"error": error_msg}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    print(f"Validation errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
