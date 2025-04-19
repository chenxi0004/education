from django.urls import path
from role.views import (
    ListAllView,
    SearchView,
    SaveView,
    ActionView,
    CheckView,
    MenusView,
    GrantView,
)

urlpatterns = [
    path("listAll", ListAllView.as_view(), name="listAll"),
    path("search", SearchView.as_view(), name="search"),  # 用户信息查询
    path("save", SaveView.as_view(), name="save"),  # 添加修改角色信息
    path("action", ActionView.as_view(), name="action"),  # 角色信息操作
    path("check", CheckView.as_view(), name="check"),
    path("menus", MenusView.as_view(), name="menus"),  # 根据角色查询菜单权限
    path("grant", GrantView.as_view(), name="grant"),  # 角色权限授权
]
