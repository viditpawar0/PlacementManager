from django.urls import path
from placements.views import *
from users.views import *
from tests.views import *
from courses.views import *
from internships.views import *

urlpatterns = [
    # Placement URLs
    path('placement/allplacements/', get_all_placements, name='get_all_placements'),
    path('placement/createplacements/', create_placement, name='create_placement'),
    path('placement/<int:id>/', get_placement_by_id, name='get_placement_by_id'),
    path('placement/course/<str:course>/', get_placements_by_course, name='get_placements_by_course'),
    path('placement/student/<str:username>/', get_placements_by_student, name='get_placements_by_student'),
    path('placement/company/<str:company>/', get_placements_by_company, name='get_placements_by_company'),
    path('placement/edit/<int:id>/', edit_placement, name='edit_placement'),
    path('placement/delete/<int:id>/', delete_placement, name='delete_placement'),

    # User URLs
    path('user/createuser/', register_user, name='create_user'),
    path('user/view/<str:username>/', view_user_by_username, name='view_user_by_username'),
    path('user/edit/<str:username>/', edit_user_by_username, name='edit_user_by_username'),
    path('user/delete/<str:username>/', delete_user_by_username, name='delete_user_by_username'),
    path('user/change_password/<str:username>/', change_password, name='change_password'),
    path('user/login/', login_user, name='login'),
    # Test URLs
    
    path('test/create/', create_test, name='create_test'),
    path('test/all/<str:course_name>/', get_tests_by_course, name='get_tests_by_course'),
    path('test/<int:test_id>/', get_test_by_id, name='get_test_by_id'),
    # Test Result URLs
    path('testresult/add/', add_test_result, name='add_test_result'),

    #cources 
    path('course/add/', add_course, name="add a course"),
    path('course/all/<str:student_id>/', get_student_courses, name='get_cources_by_studentid'),
    path('course/<int:course_id>/', get_course_details, name='get_course_details'),
    path('course/edit/<int:course_id>/', edit_course, name='edit_course'),
    
    #internships
    path('internship/add/', add_internship, name="add_internship"),
    path('internship/all/<str:student_id>/', get_student_internships, name='get_internships_by_studentid'),
    path('internship/<int:internship_id>/', get_internship_details, name='get_internship_details'),
    path('internship/edit/<int:internship_id>/', edit_internship, name='edit_internship'),

]
