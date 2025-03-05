#!/usr/bin/perl
use strict;
use warnings;

# Step 1: Clone the Repository
# Open your terminal and run:
# git clone https://github.com/AwwwRyan/PlacementManager.git
# cd PlacementManager

# Step 2: Create a Virtual Environment (Recommended)
# It’s best to use a virtual environment to manage dependencies:
# python -m venv venv

# Activate it:
# Windows (Command Prompt)
# venv\Scripts\activate

# Windows (PowerShell)
# venv\Scripts\Activate.ps1

# Mac/Linux
# source venv/bin/activate

# Step 3: Install Dependencies
# pip install -r requirements.txt

# Step 4: Run Database Migrations
# Django needs migrations to set up the database schema:
# python manage.py makemigrations
# python manage.py migrate

# Step 5: Create a Superuser (For Admin Panel)
# If you need admin access, create a superuser:
# python manage.py createsuperuser
# Follow the prompts to set a username, email, and password.

# Step 6: Run the Django Development Server
# Start the server:
# python manage.py runserver

# Step 7: Test APIs Using Postman or Curl


# USER MODULE

## Course Choices

{
    ('computer_science', 'Computer Science'),
    ('data_science', 'Data Science'),
    ('business_management', 'Business Management'),
    ('mechanical_engineering', 'Mechanical Engineering'),
    ('electrical_engineering', 'Electrical Engineering'),
    ('civil_engineering', 'Civil Engineering'),
    ('biotechnology', 'Biotechnology'),
    ('economics', 'Economics'),
}

## User Module APIs

### **POST** /api/user/createuser/

{
    "username": "new_student",
    "password": "secure_password",
    "email": "student@example.com",
    "role": "student",
    "course_pursuing": "computer_science",
    "first_name": "John",
    "last_name": "Doe"
}

### **POST** /api/user/login/

{
    "username": "new_student_aryan",
    "password": "password"
}

### **GET** /api/user/view/{username}/

### **PUT** /api/user/edit/{username}/

{
    "email": "newemail@example.com",
    "first_name": "NewFirstName",
    "last_name": "NewLastName"
}

### **POST** /api/user/change_password/

{
    "old_password": "secure_password",
    "new_password": "more_secure_password"
}

### **DELETE** /api/user/delete/{username}/


# PLACEMENT MODULE

## Placement Module APIs

### **GET** /api/placement/allplacements/

### **GET** /api/placement/{id}/

### **GET** /api/placement/{course}/

### **GET** /api/placement/student/{username}/

### **GET** /api/placement/company/{company}/

### **POST** /api/placement/createplacements/

{
    "student": "new_student",
    "company": "Google",
    "package": 1200000,
    "job_role": "Deputy Editor"
}

### **PUT** /api/placement/edit/{id}/

{
    "company": "Amazon",
    "package": 1300000
}

### **DELETE** /api/placement/delete/{id}/


# TEST MODULE

## Test Module APIs

### **POST** /api/test/create/

{
    "name": "Aptitude Test 1",
    "course": "computer_science",
    "description": "Basic aptitude test for placements",
    "syllabus": "Algebra, Probability, Logical Reasoning",
    "test_type": "aptitude",
    "duration": 60,
    "total_marks": 100,
    "date": "2025-05-15"
}

### **GET** /api/test/{test_id}/

### **GET** /api/test/{course_name}/

### **PUT** /api/test/edit/{test_id}/

{
    "name": "Updated Test Name",
    "description": "Updated test details"
}

### **DELETE** /api/test/delete/{test_id}/


## Test Result Module APIs

### **POST** /api/testresult/add/

{
    "student_username": "new_student",
    "test": 1,
    "score": 80
}

### **GET** /api/testresult/student/{username}/

### **GET** /api/testresult/test/{test_id}/

### **PUT** /api/testresult/edit/{result_id}/

{
    "score": 90
}

### **GET** /api/testresult/top/{test_id}/

# INTERNSHIP MODULE

## Internship Module APIs

### POST /api/internship/add/
{
    "student": "new_student",
    "company": "Microsoft",
    "role": "Software Intern",
    "start_date": "2025-06-01",
    "end_date": "2025-09-01",
    "description": "Worked on developing internal tools"
}

### GET /api/internship/all/{username}/

### GET /api/internship/{internship_id}/

### GET /api/internship/course/{course_pursuing}/

### PUT /api/internship/edit/{internship_id}/
{
    "role": "Backend Developer Intern",
    "company": "Microsoft"
}

# COURSES MODULE

## Courses Module APIs

### POST /api/course/add/
{
    "student": {username},
    "name": "Machine Learning Basics",
    "description": "Introduction to ML concepts",
    "duration": 40,
    "certification": true
}

### GET /api/course/all/{username}/

### GET /api/course/{course_id}/

### GET /api/course/course/{course_pursuing}/

### PUT /api/course/edit/{course_id}/
{
    "name": "Advanced Machine Learning",
    "duration": 45
}
