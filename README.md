USER MODULE

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
    
# APIs

## /api/user/createuser/

{
    "username": "new_student",
    "password": "secure_password",
    "email": "student@example.com",
    "role": "student",
    "course_pursuing": "computer_science",
    "first_name": "John",
    "last_name": "Doe"
}

## /api/user/list_all/
## /api/user/view/{username}/
## /api/user/edit/{username}/

{
    "email": "newemail@example.com",
    "first_name": "NewFirstName",
    "last_name": "NewLastName",
}

## /api/user/delete/{username}/
## /api/user/change_password/

{
    "old_password": "secure_password",
    "new_password": "more_secure_password"
}

## api/user/login/

{
    "username": "new_student_aryan",
    "password": "more_secure_password"
}
