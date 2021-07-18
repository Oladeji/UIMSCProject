from ResultApp.models import Aset, Student
from django import forms


class StudentModelForm(forms.ModelForm):
      class Meta:
        model = Student
        fields = ['matricno','surname','middlename','firstname','presentstate']


        def clean(self, *args ,**kwargs):
            matricno = self.cleaned_data.get('matricno')
            #password = self.cleaned_data.get('password')
            surname = self.cleaned_data.get('surname')
            if password != password2:
                print(password)
                print(password2)
                raise forms.ValidationError('password must match')
            email_qs = User.objects.filter(email=email)
            if email_qs.exists():
                raise forms.ValidationError('This email already exists')

        # courselist=""
        # api=settings.BASE_URL+'/api/Camp/PythonGetAvailableCoursesForEmail'
        # try:
         
        #   params={'email':email}
        #   r = requests.get(api,params)
        #   print(courselist)
        #   courselist = json.loads(r.text)
        #   print(courselist)
        #   print(r.text)
        # except Exception as inst:
        #    print (inst)
        #    raise forms.ValidationError('Problem getting Email from Server - Contact Admin')            
        # if courselist=="":
        #    raise forms.ValidationError('Problem getting Email from Server, '+ email+ ' Not Registerd')    
        # if len(courselist)==0 :
        #    raise forms.ValidationError('Lecturer Not Register For Any Course, Contact CIDM/HOD')    

            return  super(UserRegisterForm,self).clean(*args ,**kwargs)


class AsetModelForm(forms.ModelForm):
    
    class Meta:
        model = Aset
        fields = ['asetid','description']
        