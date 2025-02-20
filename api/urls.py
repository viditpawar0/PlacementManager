from django.urls import path
from placements.views import *
from users.views import *
from tests.views import *

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
    
]
