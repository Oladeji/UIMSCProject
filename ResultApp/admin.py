from ResultApp.models import Asemester, Aset,Asession,Student
from django.contrib import admin


# Register your models here.
admin.site.site_header ="PG LECTURER"
admin.site.site_title ="PG LECTURER ADMIN AREA" 
admin.site.index_title ="WELCOME TO PG LECTURER ADMIN"

#admin.site.register(Aset)

admin.site.register(Asession)
admin.site.register(Asemester)

admin.site.register(Student)



class AsessionInline(admin.TabularInline):
     model = Asession
     extra=3


class AsetAdmin(admin.ModelAdmin):
    #   fieldsets = [(None,{'fields':['PropertyName']}),
    #   ('Property Description ',{'fields':['PropertyDescription'],'classes':['collapse']}),     ]
      inlines= [AsessionInline]


admin.site.register(Aset,AsetAdmin)

