from django.db import models
from rest_framework import serializers
from role.models import SysRole


# Create your models here.
class SysMenu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, verbose_name="菜单名称")
    icon = models.CharField(max_length=100, null=True, verbose_name="菜单图标")
    parent_id = models.IntegerField(null=True, verbose_name="ID")
    order_num = models.IntegerField(null=True, verbose_name="显示顺序")
    path = models.CharField(max_length=200, null=True, verbose_name="路由地址")
    component = models.CharField(max_length=255, null=True, verbose_name="组件路径")
    MENU_TYPE_CHOICES = [
        ("M", "目录"),
        ("C", "菜单"),
        ("F", "按钮"),
    ]
    menu_type = models.CharField(
        max_length=1, choices=MENU_TYPE_CHOICES, null=True, verbose_name="菜单类型"
    )
    # menu_type = models.CharField(
    #     max_length=1, null=True, verbose_name="菜单类型(M目录c菜单F按钮)"
    # )
    perms = models.CharField(max_length=100, null=True, verbose_name="权限标识")
    create_time = models.DateField(null=True, verbose_name="创建时间")
    update_time = models.DateField(null=True, verbose_name="更新时i间")
    remark = models.CharField(max_length=500, null=True, verbose_name="")

    def _lt_(self, other):
        return self.order_num < other.order_num

    class Meta:
        db_table = "sys_menu"


class SysMenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        if hasattr(obj, "children"):
            serializerMenuList: list[SysMenuSerializer2] = list()
            for sysMenu in obj.children:
                serializerMenuList.append(SysMenuSerializer2(sysMenu).data)
            return serializerMenuList

    class Meta:
        model = SysMenu
        fields = "__all__"


class SysMenuSerializer2(serializers.ModelSerializer):
    class Meta:
        model = SysMenu
        fields = "__all__"


# 系统角色菜单关联类
class SysRoleMenu(models.Model):
    id = models.AutoField(primary_key=True)
    # role = models.ForeignKey(SysRole, on_delete=models.PROTECT)
    # menu = models.ForeignKey(SysMenu, on_delete=models.PROTECT)

    role = models.ForeignKey(
        SysRole,
        on_delete=models.PROTECT,
        related_name="menus",  # 通过角色反向查询关联的菜单
        verbose_name="角色"
    )
    menu = models.ForeignKey(
        SysMenu,
        on_delete=models.PROTECT,
        related_name="roles",  # 通过菜单反向查询关联的角色
        verbose_name="菜单"
    )

    class Meta:
        db_table = "sys_role_menu"


class SysRoleMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysRoleMenu
        fields = "__all__"
