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
