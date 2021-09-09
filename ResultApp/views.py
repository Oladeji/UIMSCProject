from UIMScApp.settings import BASE_DIR
import os
from django.http.response import HttpResponse
from ResultApp.generallibrary import downloadprocessregisteredcourses, generateCourseRegistrationData
from ResultApp.forms import AsetForm,  CourseModelForm
from ResultApp.models import Asession, Aset, Course, Student
from ResultApp.generatelist import generatelist
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage



# Create your views here.
def index(response):
    return render(response,'ResultApp/index.html');

def home(response):
    return render(response,'ResultApp/homepage.html');

def importStudents(response):
    return render(response,'ResultApp/importstudents.html');

def store_file(file):
  with open('temp/aaa.ddd','wb+') as dest:
      for chuck in file.chunks():
          dest.write(chuck)


class CreateStudentProfile(View):
  def get(self,request):
        allset= Aset.objects.all()
        return render(request,'ResultApp/addprofiles.html',{'allset':allset})


  def post(self,request):
     if request.FILES['profilefile'] :             
            #excel_file= store_file(request.FILES['profilefile'])
            excel_file=request.FILES['profilefile']
            lists,existing = generatelist(excel_file,request.POST['asetid'])
     return HttpResponseRedirect('/addprofiles')


def generate_courseregistration_data(request):
    context ={}
    thesets= Aset.objects.all()
    thesessions= Asession.objects.all()
    print('allcourses')
    context ={ 'thesets':thesets,
    'thesessions':thesessions
    }
    if request.method == 'POST' :       
        form = AsetForm(request.POST)       
        print(request.POST)
        Selectedset= request.POST['Selectedset']
        studenttype= request.POST['studenttype']
        thesession = request.POST['thesession']
        thefile = generateCourseRegistrationData(Selectedset,studenttype,thesession)

        with open( thefile,'r') as f:
            data1 =f.read()
        #data1 =  os.path.join(BASE_DIR /"temp", thefile)
        response = HttpResponse(data1,content_type='application/ms-excel')
        response['Content-Disposition'] = "attachment; filename="+Selectedset+studenttype
        return response  
    else: 
        pass
    
    
        

    return render(request,'ResultApp/generate_registration_data.html',context)

def download_process_registered_courses(request):
    context ={}
    thesets= Aset.objects.all()
    thesessions= Asession.objects.all()
    print('allcourses')
    context ={ 'thesets':thesets,
               'thesessions':thesessions
    }
    if request.method == 'POST' :       
        #form = AsetForm(request.POST)       
        print(request.POST)
        Selectedset= request.POST['Selectedset']
        studenttype= request.POST['studenttype']
        thesession = request.POST['thesession']
        print('Calling downloadprocessregisteredcourses')
        thefile = downloadprocessregisteredcourses(Selectedset,studenttype,thesession)

        with open( thefile,'r') as f:
            data1 =f.read()
        #data1 =  os.path.join(BASE_DIR /"temp", thefile)
        response = HttpResponse(data1,content_type='application/ms-excel')
        response['Content-Disposition'] = "attachment; filename="+Selectedset+studenttype
        return response  
    else: 
        pass
    
       
    return render(request,'ResultApp/download_process_registered_courses.html',context)


def course_create_view(request):
    form= CourseModelForm(request.POST or None)
    allcourses = Course.objects.all()
    if form.is_valid():
        form.save()
    form= CourseModelForm()
    context ={
        'form':form,
        'allcourses':allcourses

    }

    return render(request,'ResultApp/coursecreateform.html',context)
