from django.db import models
from user.models import SysUser
from rest_framework import serializers


# Create your models here.
# 系统角色类
class SysRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, verbose_name="角色名称")
    code = models.CharField(max_length=100, null=True, verbose_name="角色权限字符串", unique=True)
    create_time = models.DateField(null=True, verbose_name="创建时间")
    update_time = models.DateField(null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=500, null=True, verbose_name="")

    class Meta:
        db_table = "sys_role"


class SysRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysRole
        fields = "__all__"


# 系统用户角色关联类
class SysUserRole(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(SysRole, on_delete=models.PROTECT)
    user = models.ForeignKey(SysUser, on_delete=models.PROTECT)

    class Meta:
        db_table = "sys_user_role"


class SysUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUserRole
        fields = "__all__"
