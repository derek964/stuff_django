from django.db import models

# Create your models here.
#组织全称
class Dept(models.Model):
    deptcode = models.CharField(max_length=10, unique=True, primary_key=True)
    deptname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.deptname

#岗位类型(程序、策划、美术、项管)
class JobType(models.Model):
    jobtypecode = models.CharField(max_length=10, unique=True, primary_key=True)
    jobtypename = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.jobtypename

#员工岗位（客户端开发、后台开发、游戏美术3D设计、游戏美术2D设计等等）
class Job(models.Model):
    jobcode = models.CharField(max_length=10, unique=True, primary_key=True)
    jobname = models.CharField(max_length=10, unique=True)
    jobtypename = models.ForeignKey(JobType, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobname

#员工类型(正职、内包、外包、基地)
class StuffType(models.Model):
    stufftypecode = models.CharField(max_length=10, unique=True, primary_key=True)
    stufftypename = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.stufftypename

#签约公司(腾讯公司、腾娱公司)
class Company(models.Model):
    companycode = models.CharField(max_length=10, unique=True, primary_key=True)
    companyname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.companyname


# 员工状态(在职、待招)
class Status(models.Model):
    statuscode = models.CharField(max_length=10, unique=True, primary_key=True)
    statusname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.statusname

# 产品线(cymini, creativity2, Z1)
class Product(models.Model):
    productcode = models.CharField(max_length=10, unique=True, primary_key=True)
    productname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.productname

# 负责项目
# class project(models.Model):
#     projcode = models.CharField(max_length=10, unique=True, primary_key=True)
#     projname = models.CharField(max_length=10, unique=True)
#
#     def __str__(self):
#         return self.projname

class Stuff(models.Model):
    deptname = models.ForeignKey(Dept, on_delete=models.CASCADE)    #组织全程
    scode = models.CharField(max_length=10, unique=True, primary_key=True)  #员工编码
    sname = models.CharField(max_length=10, unique=True)    #姓名
    jobname = models.ForeignKey(Job, on_delete=models.CASCADE)  #所在岗位
    jobtypename = models.ForeignKey(JobType, on_delete=models.CASCADE)  # 岗位类型
    stufftypename = models.ForeignKey(StuffType, on_delete=models.CASCADE)  # 员工类型
    companyname = models.ForeignKey(Company, on_delete=models.CASCADE)  # 签约公司
    statusname = models.ForeignKey(Status, on_delete=models.CASCADE)  # 员工状态
    productname = models.ForeignKey(Product, on_delete=models.CASCADE)  # 所在产品线
    # projname = models.ForeignKey(project, on_delete=models.CASCADE)