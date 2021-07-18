import json
from ResultApp.models import Asession, Aset, RegisteredCourse, Student
from django.shortcuts import render
from  CourseFormApp.BreakIntoCoursesToRegister import BreakIntoCourselist

# Create your views here.
def homepage(response):
    return render(response,'CourseFormApp/homepage.html')

def fillcourse_form(request):
 
    
    thesessions = Asession.objects.all()
    context ={'thesessions' :thesessions ,'error':'Please supply login again ','allcourses':[]}
    print(request.session['matricno'] )

    if(not request.session['matricno']):  
       print(request.session['matricno'] )
       return render(request,'CourseFormApp/fillcourse_form.html' ,context)
    matric =request.session['matricno']



    if request.method == 'GET' :
       print('DEALING WITH GET ')    
       print(matric)
       
       

   
       #data = RegisteredCourse.objects.get()
       # data=Student.objects.get(matricno=matric).RegisteredCourse_set.all()  

    #    try:
    #        print(data)
    #        print(data.coursetoRegister)
    #    except RegisteredCourse.DoesNotExists():
    #            print (matric +' does not exists') 
    if request.method == 'POST' :  
        print('DEALING WITH POST ')     
        print(request.POST)
        # Determine the button pressed and then load RegisteredCourse 
        load = request.POST.get('loadbtn','Notloaded') 
        print(load)  
        if(load=='loadbtn'):
            thesession=request.POST.get('thesession','NoSession')  
            print(thesession )
            print(matric)
            print('this is d current sessio selected', thesession)
            if(thesession=='NoSession'):  
                return render(request,'CourseFormApp/fillcourse_form.html' ,{ 'thesessions' :thesessions ,'error':'No session selected'})           
           
            try :
                
                data=RegisteredCourse.objects.get(student__matricno=matric,asession__asessionid =thesession)  
                #data=RegisteredCourse.objects.get(student__matricno=matric)
                allcourses= BreakIntoCourselist(data.coursetoRegister,12)
                
                print(data.coursetoRegister)  
            except Exception as m:  
                print (m )     
            return render(request,'CourseFormApp/fillcourse_form.html' ,{ 'thesessions' :thesessions ,'error':'','allcourses':allcourses})           

        saveselection = request.POST.get('saveselectionbtn','Notsaveselectionbtn') 
        print(saveselection)

        if(saveselection=='saveselectionbtn'):#
            return render(request,'CourseFormApp/fillcourse_form.html' ,{ 'error':'Nothing to save for now '})           

 

    return render(request,'CourseFormApp/fillcourse_form.html' ,context)

            

def login(request):
    context ={}
    request.session['matricno']= ''
          
    if request.method == 'POST' :       
        print(request.POST)
        emailaddress= request.POST['emailaddress']
        password= request.POST['password']
        try :
          res= Student.objects.get(password=password,emailaddress=emailaddress)
          print(emailaddress)
          print(password)
          print(res)
          print("I got here...")
          names ="("+res.matricno+")"+ res.surname +", "+res.middlename+" "+res.firstname
          request.session['matricno']= res.matricno

          print(names)
          print("I got here...too")
          return render(request,'CourseFormApp/homepage.html',{"names":names})       
        except Exception as e :
            print("This is an exception")
            print(e)
            return render(request,'CourseFormApp/login.html')


    return render(request,'CourseFormApp/login.html')
    
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

