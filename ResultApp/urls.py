
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='homepage'),
    path('index',views.index,name='indexpage'),
    path('course_create',views.course_create_view,name='course_create'),
    path('generate_courseregistration_data',views.generate_courseregistration_data,name='generate_courseregistration_data'),
    path('importStudents',views.importStudents,name='importStudents'),
    path('addprofiles',views.CreateStudentProfile.as_view(),name='addprofiles'),
    
    ]
 