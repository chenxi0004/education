from django.urls import path
from menu.views import TreeListView, SaveMenuView, ActionView

urlpatterns = [
    path("treeList", TreeListView.as_view(), name="treeList"),
    path("save", SaveMenuView.as_view(), name="save"),  # 添加修改信息
    path("action", ActionView.as_view(), name="action"),  # 菜单信息操作
]
