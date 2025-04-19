from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self):
        import user.signals
        # from role.models import SysRole
        #
        # # 初始化角色
        # roles = [
        #     {"name": "管理员", "code": "admin"},
        #     {"name": "学生", "code": "student"},
        #     {"name": "教师", "code": "teacher"}
        # ]
        #
        # for role in roles:
        #     SysRole.objects.get_or_create(name=role["name"], code=role["code"])

        # from role.models import SysRole
        # from menu.models import SysMenu, SysRoleMenu
        # # 初始化菜单权限
        # student_role = SysRole.objects.get(code="student")
        # teacher_role = SysRole.objects.get(code="teacher")
        #
        # # 学生权限
        # student_menus = SysMenu.objects.filter(name__in=["课程学习", "课程资料","消息"])
        # for menu in student_menus:
        #     SysRoleMenu.objects.get_or_create(role=student_role, menu=menu)
        #
        # # 教师权限
        # teacher_menus = SysMenu.objects.filter(name__in=["课程管理","课程学习", "课程资料", "互动管理","消息"])
        # for menu in teacher_menus:
        #     SysRoleMenu.objects.get_or_create(role=teacher_role, menu=menu)
