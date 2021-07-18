
from django.urls import path
from . import views


urlpatterns = [
    path('',views.login,name='login'),
    path('homepage',views.homepage,name='homepage'),
    path('login',views.login,name='login'),
    path('fillcourse_form',views.fillcourse_form,name='fillcourse_form'),
    # path('generate_courseregistration_data',views.generate_courseregistration_data,name='generate_courseregistration_data'),
    # path('importStudents',views.importStudents,name='importStudents'),
    # path('addprofiles',views.CreateStudentProfile.as_view(),name='addprofiles'),
    
    ]
 