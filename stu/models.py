from django.db import models

# Create your models here.
class dept(models.Model):
    deptcode = models.CharField(max_length=10, unique=True, primary_key=True)
    deptname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.deptname

class project(models.Model):
    projcode = models.CharField(max_length=10, unique=True, primary_key=True)
    projname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.projname

class stuff(models.Model):
    scode = models.CharField(max_length=10, unique=True, primary_key=True)
    sname = models.CharField(max_length=10, unique=True)
    deptname = models.ForeignKey(dept, on_delete=models.CASCADE)
    projname = models.ForeignKey(project, on_delete=models.CASCADE)