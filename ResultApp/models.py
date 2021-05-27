from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import uuid
from django.urls import reverse
#import datetime

class Lecturer(User):
    

    class Meta:
        proxy = True
# Create your models here.
class Aset(models.Model):

    asetid = models.CharField( max_length=4)
    description= models.CharField(default="",max_length=50)

    def __str__(self):
      return self.asetid

class Asession(models.Model):
    aset = models.ForeignKey(Aset,on_delete=models.DO_NOTHING)
    asessionid = models.CharField( max_length=9)
    description= models.CharField(default="",max_length=50)

    def __str__(self):
      return self.asetid

class Asemester(models.Model):
    aset = models.ForeignKey(Asession,on_delete=models.DO_NOTHING)
    semesterid = models.CharField( max_length=1)
    semestername = models.CharField( max_length=20)
    description= models.CharField(default="",max_length=50)

    def __str__(self):
      return self.asetid



class Biodata(models.Model):

    matricno = models.CharField(max_length=20)
    studentGuId  = models.UUIDField( default= uuid.uuid4)
    asetid = models.ForeignKey(Aset,on_delete=models.DO_NOTHING)
    asession= models.CharField(max_length=9)
    faculty= models.CharField(max_length=30)
    department= models.CharField(max_length=40)
    programme= models.CharField(max_length=40)
    applicationnumber= models.CharField(max_length=20)
    formno= models.CharField(max_length=20)
    surname= models.CharField(max_length=30)
    middlename= models.CharField(max_length=30)
    firstname= models.CharField(max_length=30)
    presentstate= models.CharField(max_length=20)#student,graduate,suspended,leave,withdraw
    graduatingsession= models.CharField(max_length=9)
    emailaddress= models.CharField(max_length=40)
    phonenumber= models.CharField(max_length=40)
    fieldofinterest= models.CharField(max_length=40)
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


class Student(models.Model):
    biodata = models.OneToOneField(Biodata,on_delete=models.DO_NOTHING)
    matricno = models.CharField(max_length=20,primary_key=True)


class StudentDocument(models.Model):
     student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
     document = models.FileField();
     dateuploaded= models.DateField('Payment Date',default=timezone.now())
     thesessionofinterest= models.CharField(max_length=9)
     description= models.CharField(default="",max_length=50)

     def __str__(self):
       return f" {self.description}  For  {self.studentDocumentId.matricno}"


class Course(models.Model):
    semester = models.ForeignKey(Asemester,on_delete=models.DO_NOTHING)
    coursecode = models.CharField(max_length= 6)
    coursename = models.CharField(max_length= 30)
    coursenature = models.CharField(max_length= 1)# compulsory , elective ,require
    passmark = models.IntegerField()
    courseunit = models.IntegerField();
    courseGuId  = models.UUIDField( default= uuid.uuid4)


class RegisteredCourse(models.Model):
    coursetoRegister = models.ManyToManyField(Course,related_name="toregister")
    registeredCourses = models.ManyToManyField(Course,related_name="alreadyregistered")
    student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)         
    dateregistered =  models.DateField('Registered Date',default=timezone.now())
    status = models.CharField(max_length=20)
    totalregisteredunit = models.SmallIntegerField()
    maxpossibleunit = models.SmallIntegerField()
    minpossibleunit = models.SmallIntegerField()

class Supervisors(models.Model):
      student = models.ManyToManyField(Student) 
      supervisor = models.ManyToManyField(Lecturer)  

class SessionRegistration(models.Model):
    student = models.ManyToManyField(Student) 
    aset = models.ForeignKey(Asession,on_delete=models.DO_NOTHING)


class DetailResult(models.Model):
     student = models.ManyToManyField(Student) 
     course = models.ManyToManyField(Course)
     score  = models.SmallIntegerField()
     readonly = models.BooleanField(default=False)
     passed = models.BooleanField(default=False)
     donedate =  models.DateField('Registered Date',default=timezone.now())
     theuser  = models.ManyToManyField(Lecturer)     
 