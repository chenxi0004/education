from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Teacher

# # 自定义注册模型到管理后台
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ("student_id", "student_name", "gender", "school", "phone_number")  # 在列表页显示的字段
#     search_fields = ("student_name", "student_id")  # 添加搜索框
#     list_filter = ("gender", "school")  # 添加筛选器
#
#
# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ("teacher_id", "teacher_name", "gender", "school", "phone_number", "email")
#     search_fields = ("teacher_name", "teacher_id")
#     list_filter = ("gender", "school")


admin.site.register(Student)
admin.site.register(Teacher)
