from django.db import models

# Create your models here.
# class SysUser(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100, unique=True, verbose_name="")
#     password = models.CharField(max_length=100, verbose_name="")
#     avatar = models.CharField(max_length=255, null=True, verbose_name="用户头像")
#     email = models.CharField(max_length=100, null=True, verbose_name="")
#     phonenumber = models.CharField(max_length=11, null=True, verbose_name="手机号码")
#     login_date = models.DateField(null=True, verbose_name="最后登录时间")
#     status = models.IntegerField(null=True, verbose_name="帐号状态(0正常 1停用)")
#     create_time = models.DateField(null=True, verbose_name="创建新时间")
#     update_time = models.DateField(null=True, verbose_name="更新时间")
#     remark = models.CharField(max_length=500, null=True, verbose_name="备注")

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.core.validators import RegexValidator
#
# class SysUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The given username must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(username, password, **extra_fields)
#
#
# class SysUser(AbstractBaseUser, PermissionsMixin):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
#     password = models.CharField(max_length=128, verbose_name="密码")
#     avatar = models.ImageField(upload_to='avatars/', null=True, verbose_name="用户头像")
#     email = models.EmailField(max_length=100, null=True, verbose_name="邮箱")
#     phonenumber = models.CharField(
#         validators=[RegexValidator(regex=r'^1[3-9]\d{9}$', message="手机号码格式不正确")],
#         max_length=11, null=True, verbose_name="手机号码"
#     )
#     login_date = models.DateTimeField(null=True, verbose_name="最后登录时间")
#     status = models.IntegerField(
#         choices=[(0, '正常'), (1, '停用')],
#         default=0, verbose_name="帐号状态"
#     )
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
#     remark = models.CharField(max_length=500, null=True, verbose_name="备注")
#     last_login = models.DateTimeField(null=True, blank=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#
#     objects = SysUserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         db_table = "user_sysuser"


from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from rest_framework import serializers


# from role.models import SysRole, SysUserRole

class SysUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        # # 默认分配学生角色
        # student_role = SysRole.objects.get(code="student")
        # SysUserRole.objects.create(user=user, role=student_role)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)


class SysUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    avatar = models.CharField(max_length=255, null=True, verbose_name="用户头像")
    email = models.CharField(max_length=100, null=True, verbose_name="邮箱")
    phonenumber = models.CharField(max_length=11, null=True, verbose_name="手机号码")
    login_date = models.DateField(null=True, verbose_name="最后登录时间")
    status = models.IntegerField(null=True, verbose_name="帐号状态(1正常 0停用)", default=1)
    create_time = models.DateField(null=True, verbose_name="创建时间")
    update_time = models.DateField(null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=500, null=True, verbose_name="备注")
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # 添加性别字段
    GENDER_CHOICES = [
        (0, '男'),
        (1, '女'),
        (2, '其他')
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, verbose_name="性别")

    # 添加学生/教师编号字段
    student_or_teacher_id = models.CharField(max_length=20, unique=True, null=True, verbose_name="学生/教师编号")

    objects = SysUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]  # 添加 REQUIRED_FIELDS 属性

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user_sysuser"


class SysUserserializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = "__all__"
