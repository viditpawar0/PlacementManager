from placements.views import *
from users.views import *
from django.urls import path

urlpatterns = [
    path('placement/allplacements/', get_all_placements, name='get_all_users'),
    path('placement/createplacements/', create_placement, name='create_placement'),
    path('user/createuser/',register_user, name='create_user')
]
