


from django.db.models.fields import NullBooleanField
from UIMScApp.settings import BASE_DIR
import os
from ResultApp.models import Asession, Aset, Course, DetailResult, RegisteredCourse, Student

def filltowidth(word,lent):

    while len(word)< lent:
        word +=" "
    return word

def downloadprocessregisteredcourses(theset , thelevel,thesession):
        print('Inside Calling downloadprocessregisteredcourses')
        filename = os.path.join(BASE_DIR /"temp",theset + thelevel) +'.txt'   
        #maxwidth=100
        #allnewcourses = Course.objects.filter(courselevel=thelevel)
        #thesets= Aset.objects.get(asetid=theset)
        selectedsession= Asession.objects.get(asessionid=thesession)
        print(selectedsession)
        allregstudents= RegisteredCourse.objects.filter(asession=selectedsession,status="FINAL")
        print("allregstudents")
        print(allregstudents)
        allcourses=  Course.objects.all()
        print("allcourses \n")
        print(allcourses)
        with open( filename,'w+') as f:
          for reg in allregstudents :
            print(reg.status," --- ", reg.student.matricno)
            processCourseList4Registration(reg.registeredCourses,allcourses)
            f.write(filltowidth (reg.status,20)+ "_\n")
             
        f.close
        print(' From method :'+filename)
        return filename

def returnNormalCourses(courses,lent):
    packed=''
    for crs in courses:
        packed += filltowidth(crs.coursecode,6) +filltowidth(str(crs.courseunit ),2)+filltowidth(crs.coursenature,2)+'N_'
    return packed


def processCourseList4Registration(registeredCourses,allcourses):

    courselist = BreakregisteredCoursesIntoEach(registeredCourses)
    coursefoundlist,notfoundlist = Separateavailablecourse(courselist,allcourses)
    print("FOUND COURSES")
    print (coursefoundlist)
    print("/n")
    print("NOT Found list")
    print(notfoundlist)
    #registerCourses(coursefoundlist)
    return ""


def  Separateavailablecourse(courselist,allcourses):
   coursefoundlist=[]
   notfoundlist =[]
   for crs in courselist :       
        detail ,found =locatespecificcourse(crs['code'],allcourses)
        if found :
           print(" the detail for is below " ,crs['code'] ,"\n")
           coursefoundlist.append(detail)
        else :
            notfoundlist.append(detail) 
   return coursefoundlist,notfoundlist


def locatespecificcourse(crs ,allcourses):
    for course in allcourses :
        if crs == course.coursecode :        
          return course,True
    return crs,False 



def registerCourses(courselist): 
    # for crs in courselist :
    #      try :
    #         obj,created= DetailResult.objects.get_or_create(    
    #                             student = student, 
    #                             defaults={ 
    #                             'studentGuId'  :  uuid.uuid4(),
    #                             'course' : course, 
    #                             'score' : score,
    #                             'readonly' : readonly,
    #                             'passed' : passed,
    #                             'donedate' : donedate,
    #                             'registeredDate': default=timezone.now()
                                      
    #                            })  
    #      except Exception as inst:
    #                         print("I  raise error on => ", matricno)
    #                         print(inst)   
    #      if created :
    #         studentlist.append(obj)
    #      else:
    #         existinglist.append(obj)
    #                 #ns.save()
    #         print(obj)
    print(courselist)
    


def generateCourseRegistrationData(theset , thelevel,thesession):
        filename = os.path.join(BASE_DIR /"temp",theset + thelevel) +'.txt'
        #filename = theset + thelevel +'.txt'
        #with open( os.path.join(BASE_DIR /"temp", filename),'w+') as f:
    
    
        maxwidth=100
        allnewcourses = Course.objects.filter(courselevel=thelevel)
        thesets= Aset.objects.get(asetid=theset)
        selectedsession= Asession.objects.get(asessionid=thesession)
        print(selectedsession)
        allstudents = thesets.student_set.all() 
        print("All courses and students are printed below =========")
        with open( filename,'w+') as f:
 
            for stu in allstudents :
                obj, created = RegisteredCourse.objects.get_or_create(
                    coursetoRegister = filltowidth( returnNormalCourses(allnewcourses,180),250),
                    registeredCourses = '',
                    student = stu,       
                    #dateregistered = timezone.now(),'
                    status = 'PENDING',
                    totalregisteredunit = 0,
                    maxpossibleunit = thesets.MinimumGraduatingUnit,
                    minpossibleunit = thesets.MinimumGraduatingUnit,
                    asession= selectedsession)
                          

                print("GG"+filltowidth  ( stu.matricno,20) +"_"  +filltowidth ( stu.surname,20)           + "_" +filltowidth ( returnNormalCourses(allnewcourses,maxwidth),180) + "_1\n") 
                Status= 'OLD : '
                if created :
                    Status= 'NEW : '
                f.write(filltowidth (stu.matricno,20)+"_"+filltowidth(stu.surname,20)+ "_"+filltowidth( returnNormalCourses(allnewcourses,maxwidth),180)+ "_\n")
             
            f.close
        print(' From method :'+filename)
        return filename

def BreakregisteredCoursesIntoEach(data,step=6):
   eachcourselist = []
   print(data)
   print(len(data))
   print(int(len(data)/step))
   for i in range(int(len(data)/step)):
      achunk = data[i*step:i*step+step]   

      if((achunk[:6]) .strip()!=""):
         alist = {'code' : achunk[:6],
           }
         eachcourselist.append(alist)
         print(i,alist)
   print('eachcourselist',eachcourselist)
   return  eachcourselist   