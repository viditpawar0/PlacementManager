# USER MODULE

## Cource Choices

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

### /api/user/createuser/

{
    "username": "new_student",
    "password": "secure_password",
    "email": "student@example.com",
    "role": "student",
    "course_pursuing": "computer_science",
    "first_name": "John",
    "last_name": "Doe"
}

### api/user/login/

{
    "username": "new_student_aryan",
    "password": "password"
}

### /api/user/view/{username}/

### /api/user/edit/{username}/

{
    "email": "newemail@example.com",
    "first_name": "NewFirstName",
    "last_name": "NewLastName",
}

### /api/user/change_password/

{
    "old_password": "secure_password",
    "new_password": "more_secure_password"
}

### /api/user/delete/{username}/


# PLACEMENT MODULE

## Placement Module APIs

### /api/placement/allplacements/

### /api/placement/{id}/

### /api/placement/{course}/

### /api/placement/student/{username}/

### /api/placement/company/{company}/

### /api/placement/createplacements/

{
    "student": {username},
    "company": "Google",
    "package": 1200000,
    "job_role": "Deputy Editor",
}

### /api/placement/edit/{id}/

{
    "company": "Amazon",
    "package": 1300000,
}

### /api/placement/delete/{id}/

# TEST MODULE

## Test Module APIs

### /api/test/create/

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

### /api/test/{test_id}/

### /api/test/{course_name}/

### /api/test/edit/{test_id}/

{
"name": "Updated Test Name",
"description": "Updated test details"
}

### /api/test/delete/{test_id}/

## Test Result Module APIs

### /api/testresult/add/

{
"student_username": "new_student",
"test": 1,
"score": 80
}

### /api/testresult/student/{username}/

### /api/testresult/test/{test_id}/

### /api/testresult/edit/{result_id}/

{
"score": 90
}

### /api/testresult/top/{test_id}/
