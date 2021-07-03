from ResultApp.models import Aset, Student
import openpyxl
import uuid

def generatelist(excel_file,asetid):
    print("Starting............")
    wb = openpyxl.Workbook()        
    wb = openpyxl.load_workbook(excel_file)
    ws = wb["Students"]
    row_start=2
    total = ws.max_row
    studentlist=[]
    existinglist=[]
    myaset= Aset.objects.get(asetid=asetid)
    try :

            for i in range(row_start,total+ row_start):
                  
                  matricno = ws.cell(i, 1).value
                  print(i,matricno)
                  if matricno is not None:                         
                        #    created= Student.objects.create(    
                        #         matricno = matricno,  
                        #         studentGuId  =  uuid.uuid4(),
                        #         asetid = myaset,    
                        #         asession= '',   
                        #         faculty= '',    
                        #         department= '',
                        #         programme= '',  
                        #         applicationnumber= '',
                        #         formno= '',     
                        #         surname= '',  
                        #         middlename= '', 
                        #         firstname='',
                        #         presentstate= '',#student,graduate,suspended,leave,withdraw
                        #         graduatingsession=''})    

                        obj,created= Student.objects.get_or_create(    
                                matricno = matricno, 
                                defaults={ 
                                'studentGuId'  :  uuid.uuid4(),
                                'asetid' : myaset,    
                                'asession': '',   
                                'faculty': '',    
                                'department': '',
                                'programme': '',  
                                'applicationnumber': '',
                                'formno': '',     
                                'surname': '',  
                                'middlename': '', 
                                'firstname':'',
                                'presentstate': '',#student,graduate,suspended,leave,withdraw
                                'graduatingsession':''})   
                        if created :
                            studentlist.append(obj)
                        else:
                            existinglist.append(obj)
                        #ns.save()
                        
    except  Exception as inst:
          print("I am raise error => ", matricno)
          print(inst)   
                         
    return studentlist, existinglist
            
