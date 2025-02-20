from django.contrib import admin
# Register your models here.
from .models import Test
from .models import TestResult  

admin.site.register(Test)
admin.site.register(TestResult)