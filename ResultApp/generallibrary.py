


from UIMScApp.settings import BASE_DIR
import os
from ResultApp.models import Asession, Aset, Course, RegisteredCourse, Student

def filltowidth(word,lent):

    while len(word)< lent:
        word +=" "
    return word


def returnNormalCourses(courses,lent):
    packed=''
    for crs in courses:
        packed += filltowidth(crs.coursecode,6) +filltowidth(str(crs.courseunit ),2)+filltowidth(crs.coursenature,2)+'N_'
    return packed


def generateCourseRegistrationData(theset , thelevel,thesession):
        filename = os.path.join(BASE_DIR /"temp",theset + thelevel) +'.txt'
        #filename = theset + thelevel +'.txt'
        #with open( os.path.join(BASE_DIR /"temp", filename),'w+') as f:
    
        with open( filename,'w+') as f:
    
            maxwidth=100
            allnewcourses = Course.objects.filter(courselevel=thelevel)
            thesets= Aset.objects.get(asetid=theset)
            selectedsession= Asession.objects.get(asessionid=thesession)
            print(selectedsession)
            allstudents = thesets.student_set.all() 
            print("All courses and students are printed below =========")
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
