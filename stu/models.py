from django.db import models

# Create your models here.
#组织全称 部门名称
class Dept(models.Model):
    deptcode = models.CharField(max_length=10, unique=True, primary_key=True)
    deptname = models.CharField(max_length=10, unique=True, verbose_name="部门")

    def __str__(self):
        return self.deptname

#岗位类型(程序、策划、美术、项管)
class JobType(models.Model):
    jobtypecode = models.CharField(max_length=10, unique=True, primary_key=True)
    jobtypename = models.CharField(max_length=10, unique=True, verbose_name="岗位类型")

    def __str__(self):
        return self.jobtypename

#员工岗位（客户端开发、后台开发、游戏美术3D设计、游戏美术2D设计等等）
class Job(models.Model):
    jobcode = models.CharField(max_length=10, unique=True, primary_key=True)
    jobname = models.CharField(max_length=10, unique=True, verbose_name="岗位名称")
    jobtypename = models.ForeignKey(JobType, on_delete=models.CASCADE, verbose_name="岗位类型")

    def __str__(self):
        return self.jobname

# 产品线(cymini, creativity2, Z1)
class Product(models.Model):
    productcode = models.CharField(max_length=10, unique=True, primary_key=True)
    productname = models.CharField(max_length=10, unique=True, verbose_name="产品线")

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
    stuff_status = models.TextChoices('status', '在职 待招')
    stuff_type = models.TextChoices("type", "正职 内包 外包 基地")
    stuff_company = models.TextChoices("company", "腾讯公司 腾娱公司")
    deptname = models.ForeignKey(Dept, on_delete=models.CASCADE, verbose_name="组织全称")    #组织全称
    scode = models.CharField(max_length=10, unique=True, primary_key=True, verbose_name="员工编码")  #员工编码
    sname = models.CharField(max_length=10, unique=True, verbose_name="姓名")    #姓名
    jobname = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="所在岗位")  #所在岗位
    # jobtypename = models.ForeignKey(JobType, on_delete=models.CASCADE, verbose_name="岗位类型")  # 岗位类型
    stufftypename = models.CharField(blank=True, choices=stuff_type.choices, max_length=10, verbose_name="员工类型")  # 员工类型
    companyname = models.CharField(blank=True, choices=stuff_company.choices, max_length=10,verbose_name="签约公司")  # 签约公司
    status = models.CharField(blank=True, choices=stuff_status.choices, max_length=10, verbose_name="状态")  # 员工状态
    productname = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="所在产品线")  # 所在产品线
    # projname = models.ForeignKey(project, on_delete=models.CASCADE)

    def __str__(self):
        return self.sname