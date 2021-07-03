from django import forms
from .models import Aset, Course


IALLSET_CHOICES= Aset.objects.all()
class CourseModelForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ['asemester','coursecode','coursename','coursenature',
                  'passmark','courseunit','courselevel'
                  #,'courseGuId' 
                  ]

class AsetForm(forms.Form ):
    #Sets  = forms.CharField(max_length=4, widget=forms.ChoiceField.TextInput(attrs={'placeholder':'Enter Username' ,'class': 'input-line full-width','required':True}))
    Sets = forms.ChoiceField()
    #Sets= forms.CharField(label='The Set of Interest', widget=forms.Select(choices=FRUIT_CHOICES))



class AsetModelForm(forms.ModelForm):
    
    class Meta:
        model = Aset
        fields = ['asetid','description']

