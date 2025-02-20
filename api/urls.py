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
    # User URLs
    path('user/createuser/', register_user, name='create_user'),
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
