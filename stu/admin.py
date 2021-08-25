from django.contrib import admin
from stu.models import *

# Register your models here.
class NewDept(admin.ModelAdmin):
    list_display = [ 'deptname']

class NewJobType(admin.ModelAdmin):
    list_display = ['jobtypecode', 'jobtypename']

class NewJob(admin.ModelAdmin):
    list_display = ['jobcode', 'jobname']

class NewProduct(admin.ModelAdmin):
    list_display = ['productcode', 'productname']

# class Newproject(admin.ModelAdmin):
#     list_display = ['projcode', 'projname']

class NewStuff(admin.ModelAdmin):
    list_display = ['deptname', 'scode', 'sname', 'jobname', 'jobtypename', 'stufftypename', 'companyname', 'status', 'productname']

admin.site.register(Dept, NewDept)
admin.site.register(JobType, NewJobType)
admin.site.register(Job, NewJob)
admin.site.register(Product, NewProduct)
# admin.site.register(project, Newproject)
admin.site.register(Stuff, NewStuff)