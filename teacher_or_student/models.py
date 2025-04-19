from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name="学生编号")
    student_name = models.CharField(max_length=50, verbose_name="学生姓名")
    gender = models.CharField(max_length=10, choices=[("男", "男"), ("女", "女")], verbose_name="性别")
    school = models.CharField(max_length=100, verbose_name="学校")
    phone_number = models.CharField(max_length=11, verbose_name="手机号码")

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = "student"


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name="教师编号")
    teacher_name = models.CharField(max_length=50, verbose_name="教师姓名")
    school = models.CharField(max_length=100, verbose_name="学校/单位")
    gender = models.CharField(max_length=10, choices=[("男", "男"), ("女", "女")], verbose_name="性别")
    phone_number = models.CharField(max_length=11, verbose_name="手机号码")
    email = models.EmailField(verbose_name="电子邮箱")

    def __str__(self):
        return self.teacher_name

    class Meta:
        db_table = "teacher"
