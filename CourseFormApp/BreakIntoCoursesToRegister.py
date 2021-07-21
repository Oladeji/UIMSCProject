
def BreakIntoCourselist(data,step):
   courselist = []
   print(data)
   print(len(data))
   print(int(len(data)/step))
   for i in range(int(len(data)/step)):
      achunk = data[i*step:i*step+step]   

      if((achunk[:6]) .strip()!=""):
         alist = {'code' : achunk[:6],'unit':achunk[8:10],'nature':achunk[10:12]
           }
         courselist.append(alist)
         print(i,alist)
   print('courselist',courselist)
   return  courselist   

def ExtractSelectedCourses( Posted , thelist):
   finallist=[]
   print("inside ExtractSelectedCourses")
   print(Posted)
   print(thelist)
   for crs in  thelist :
      thecode=crs['code']
      print('from origibal list', thecode)
      ans= Posted.get(thecode,'NOTFOUND') 
      if(ans != 'NOTFOUND') :
         finallist.append(thecode)
      print ("\n")
          # load = request.POST.get('loadbtn','Notloaded') 
           #emailaddress= request.POST['emailaddress']
   return finallist