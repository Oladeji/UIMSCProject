from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from django.urls import reverse
#import datetime
# 
# class Lecturer(User):
    

#     class Meta:
#         proxy = True

# Create your models here.


class Supervisors(models.Model):
   description= models.CharField(default="",max_length=50)

class Aset(models.Model):
    asetid = models.CharField( max_length=4,primary_key=True)
    MinimumGraduatingUnit= models.SmallIntegerField(default=0)
    MinimumCompulsoryUnit= models.SmallIntegerField(default=0)
    MinimumElectiveUnit= models.SmallIntegerField(default=0)
    MinimumRequiredUnit= models.SmallIntegerField(default=0)
    description= models.CharField(default="",max_length=50)

    def __str__(self):
      return self.asetid

class Asession(models.Model):
    #aset = models.ForeignKey(Aset,on_delete=models.DO_NOTHING)
    asessionid = models.CharField( max_length=9)
    description= models.CharField(default="",max_length=50)

    def __str__(self):
      return f"{self.asessionid }"

class Asemester(models.Model):
    asession = models.ForeignKey(Asession,on_delete=models.DO_NOTHING)
    semesterid = models.CharField( max_length=1)
    semestername = models.CharField( max_length=20)
    description= models.CharField(default="",max_length=50)

    def __str__(self):
      return f"{self.asession.aset.asetid } ,  {self.asession.asessionid } ,{self.semesterid } {self.semestername }"


class Student(models.Model):
   
    presentstate_CHOICES=[
        ('STUDENT','STUDENT'),
        ('GRADUATE','GRADUATE'),
        ('SUSPENDED','SUSPENDED'),
        ('LEAVE','LEAVE'),
        ('WITHDRAW','WITHDRAW'),
       ('ABSENT','ABSENT'),
    ]
    matricno = models.CharField(max_length=20,primary_key=True)
    studentGuId  = models.UUIDField( default= uuid.uuid4)
    aset = models.ForeignKey(Aset,on_delete=models.DO_NOTHING)
    asession= models.CharField(max_length=9)
    faculty= models.CharField(max_length=30)
    department= models.CharField(max_length=40)
    programme= models.CharField(max_length=40)
    option= models.CharField(max_length=40 ,default="A")
    applicationnumber= models.CharField(max_length=20)
    formno= models.CharField(max_length=20)
    surname= models.CharField(max_length=30)
    middlename= models.CharField(max_length=30 ,default ='' ,blank=True)
    firstname= models.CharField(max_length=30)
    presentstate= models.CharField(max_length=20,choices= presentstate_CHOICES)#student,graduate,suspended,leave,withdraw
    graduatingsession= models.CharField(max_length=9)
    emailaddress= models.EmailField(max_length=50,default='MscDefault@ui.ng')
    phonenumber= models.CharField(max_length=40, default='234')
    password= models.CharField(max_length=50,default='000')
    def __str__(self):
        return  f"{self.matricno} : {self.surname} {self.middlename} {self.firstname }"


class Biodata(models.Model):
    student = models.OneToOneField(Student,on_delete=models.DO_NOTHING)  
    fieldofinterest= models.CharField(max_length=60)
    contactaddress= models.CharField(max_length=50)
    nationality= models.CharField(max_length=30)
    state= models.CharField(max_length=30)
    localgovt= models.CharField(max_length=30)
    modeofstudy= models.CharField(max_length=30)
    nextofkinnames= models.CharField(max_length=50)
    nextofkinaddress= models.CharField(max_length=50)
    nextofkinphoneno= models.CharField(max_length=50)
    nextofkinrelationship= models.CharField(max_length=50)
    maritalstatus= models.CharField(max_length=20)
    gender= models.CharField(max_length=20)
    password= models.CharField(max_length=50)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Biodata_detail", kwargs={"pk": self.pk})
        #return reverse("Biodata_detail", args=[ self.id])



class StudentDocument(models.Model):
     student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
     document = models.FileField(upload_to="mscdocuments",null=True);
     dateuploaded= models.DateField('Payment Date',default=timezone.now())
     thesessionofinterest= models.CharField(max_length=9)
     description= models.CharField(default="",max_length=50)

     def __str__(self):
       return f" {self.description}  For  {self.studentDocumentId.matricno}"


class Course(models.Model):
    Required='R'
    Elective='E'
    Compulsory='R'
    
    Course_CHOICES=[
        (Required,'Required'),
        (Elective,'Elective'),
        (Compulsory,'Compulsory'),
       
    ]
    asemester     = models.ForeignKey(Asemester,on_delete=models.DO_NOTHING)
    coursecode   = models.CharField(max_length= 6)
    courselevel   = models.CharField(max_length= 1,default=0)
    coursename   = models.CharField(max_length= 30)
    coursenature = models.CharField(max_length= 1,choices=Course_CHOICES)# compulsory , elective ,require
    passmark     = models.IntegerField(default=40)
    courseunit   = models.IntegerField(default=0)
    courseGuId   = models.UUIDField( default= uuid.uuid4)

    def __str__(self):
       return f"{self.coursename} @ {self.asemester.asession.asessionid } ,{self.asemester.semesterid } Level : {self.courselevel} "


class RegisteredCourse(models.Model):
    #coursetoRegister = models.ForeignKey(Course,on_delete=models.DO_NOTHING,related_name="toregister")      
    #registeredCourses = models.ForeignKey(Course,on_delete=models.DO_NOTHING,related_name="alreadyregistered")      
    coursetoRegister = models.CharField(max_length= 300)
    registeredCourses = models.CharField(max_length= 300)
    
    student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)         
    dateregistered =  models.DateField('Registered Date',default=timezone.now())
    status = models.CharField(max_length=20)
    totalregisteredunit = models.SmallIntegerField()
    maxpossibleunit = models.SmallIntegerField()
    minpossibleunit = models.SmallIntegerField()
    asession = models.ForeignKey(Asession,on_delete=models.DO_NOTHING) 

    def __str__(self):
       return f"{self.student.matricno} "
       #@ {self.asemester.asession.asessionid } ,{self.asemester.semesterid } Level : {self.courselevel} "


class SessionRegistration(models.Model):
    student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    aset = models.ForeignKey(Asession,on_delete=models.DO_NOTHING)


class DetailResult(models.Model):
     student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
     course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
     score  = models.SmallIntegerField()
     readonly = models.BooleanField(default=False)
     passed = models.BooleanField(default=False)
     donedate =  models.DateField('Registered Date',default=timezone.now())
#     theuser  = models.ForeignKey(Lecturer,on_delete=models.DO_NOTHING)  
 