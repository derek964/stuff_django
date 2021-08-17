from django.contrib import admin
from stu.models import *

# Register your models here.

class Newdept(admin.ModelAdmin):
    list_display = ['deptcode','deptname']

class Newproject(admin.ModelAdmin):
    list_display = ['projcode', 'projname']

class Newstuff(admin.ModelAdmin):
    list_display = ['scode','sname','deptname','projname']

admin.site.register(dept,Newdept)
admin.site.register(project, Newproject)
admin.site.register(stuff, Newstuff)
