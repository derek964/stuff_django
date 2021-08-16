# stuff_django

## 创建一个人员信息登记和查看的系统
包含录入人员信息：stuff，以及可查看相关人员信息的系统
主要方便共享查阅

**表deptname:**
- deptcode 部门编码（主键）
- deptname 部门名称

**表project:**
- projcode 项目编码
- projname 项目名称

**表stuff:**
- scode 编码(主键)
- sname 姓名
- deptcode 所在部门编码（外健）
- projcode 所在项目（外健）