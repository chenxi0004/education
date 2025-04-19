from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import SysUser
from role.models import SysRole, SysUserRole
from teacher_or_student.models import Student, Teacher
from django.contrib import messages
import logging


@receiver(post_save, sender=SysUser)
def assign_default_role(sender, instance, created, **kwargs):
    # 避免递归调用
    if hasattr(instance, '_role_assigned'):
        return
    # if created:
    #     student_role, _ = SysRole.objects.get_or_create(code="student", defaults={"name": "学生"})
    #     SysUserRole.objects.create(user=instance, role=student_role)
    # 确保 student_role 在所有情况下都被定义
    student_role, _ = SysRole.objects.get_or_create(code="student", defaults={"name": "学生"})
    teacher_role, _ = SysRole.objects.get_or_create(code="teacher", defaults={"name": "教师"})
    if created:
        # 新用户创建时分配默认学生角色
        SysUserRole.objects.create(user=instance, role=student_role)
    # 检查用户是否输入了学生/教师编号
    if instance.student_or_teacher_id:
        with transaction.atomic():  # 使用事务确保操作的原子性
            # 查询学生表
            try:
                student = Student.objects.get(student_id=instance.student_or_teacher_id)
                # 如果查询到学生，分配学生角色
                SysUserRole.objects.create(user=instance, role=student_role)
                # instance.status = True  # 设置状态为 1
                # 设置标志位，防止递归调用
                instance._role_assigned = True
                instance.save()  # 保存用户状态
                print(f"用户 {instance.username} 被分配为学生角色，关联学生编号: {student.student_id}")
            except Student.DoesNotExist:
                # 查询教师表
                try:
                    teacher = Teacher.objects.get(teacher_id=instance.student_or_teacher_id)
                    # 如果查询到教师，分配教师角色
                    # teacher_role, _ = SysRole.objects.get_or_create(code="teacher", defaults={"name": "教师"})
                    SysUserRole.objects.create(user=instance, role=teacher_role)
                    # instance.status = True  # 设置状态为 1
                    # 设置标志位，防止递归调用
                    instance._role_assigned = True
                    instance.save()  # 保存用户状态
                    print(f"用户 {instance.username} 被分配为教师角色，关联教师编号: {teacher.teacher_id}")
                except Teacher.DoesNotExist:
                    print(f"未找到对应的学生或教师编号: {instance.student_or_teacher_id}")
    else:
        # 如果没有输入学生/教师编号，分配默认学生角色
        SysUserRole.objects.create(user=instance, role=student_role)
        print(f"用户 {instance.username} 被分配为默认学生角色")
