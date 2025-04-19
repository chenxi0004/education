import json
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.permissions import IsAuthenticated

from menu.models import SysMenu, SysMenuSerializer, SysRoleMenu


# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework_simplejwt.authentication import JWTAuthentication
# class TreeListView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
class TreeListView(View):
    permission_classes = (IsAuthenticated,)

    # 构建菜单树
    def buildTreeMenu(self, sysMenuList):
        resultMenuList: list[SysMenu] = list()
        for menu in sysMenuList:
            # 寻找子节点
            for e in sysMenuList:
                if e.parent_id == menu.id:
                    if not hasattr(menu, "children"):
                        menu.children = list()
                    menu.children.append(e)
            # 判断父节点
            if menu.parent_id == 0:
                resultMenuList.append(menu)
        return resultMenuList

    # def buildTreeMenu(self, sysMenuList):
    #     menu_dict = {menu.id: menu for menu in sysMenuList}  # 将菜单存储到字典中
    #     root_menus = []
    #
    #     for menu in sysMenuList:
    #         if menu.parent_id == 0:
    #             root_menus.append(menu)
    #         else:
    #             parent_menu = menu_dict.get(menu.parent_id)
    #             if parent_menu and not hasattr(parent_menu, "children"):
    #                 parent_menu.children = []
    #             parent_menu.children.append(menu)
    #
    #     return root_menus
    def get(self, request, *args, **kwargs):
        menuQuerySet = SysMenu.objects.order_by("order_num")
        menuList = self.buildTreeMenu(menuQuerySet)
        sysMenuList: list[SysMenu] = menuList
        serializerMenuList: list[SysMenuSerializer] = list()
        for sysMenu in sysMenuList:
            serializerMenuList.append(SysMenuSerializer(sysMenu).data)
        # serializerMenuList = SysMenuSerializer(sysMenuList, many=True).data
        return JsonResponse({"code": 200, "treeList": serializerMenuList})


class SaveMenuView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        if data["id"] == -1:  # 添加
            obj_sysMenu = SysMenu(
                name=data["name"],
                icon=data["icon"],
                parent_id=data["parent_id"],
                order_num=data["order_num"],
                path=data["path"],
                component=data["component"],
                menu_type=data["menu_type"],
                perms=data["perms"],
                remark=data["remark"],
            )
            obj_sysMenu.create_time = datetime.now().date()
            obj_sysMenu.save()
        else:  # 修改
            obj_sysMenu = SysMenu(
                id=data["id"],
                name=data["name"],
                icon=data["icon"],
                parent_id=data["parent_id"],
                order_num=data["order_num"],
                path=data["path"],
                component=data["component"],
                menu_type=data["menu_type"],
                perms=data["perms"],
                remark=data["remark"],
                create_time=data["create_time"],
                update_time=data["update_time"],
            )
            obj_sysMenu.update_time = datetime.now().date()
            obj_sysMenu.save()
        return JsonResponse({"code": 200, "msg": "操作成功"})


# class ActionView(View):
#     def get(self, request):
#         # 尝试解析请求体
#         data = json.loads(request.body.decode('utf-8'))
#         id = data.get('id')
#         # id = request.GET.get('id')
#         menu_object: SysMenu = SysMenu.objects.get(id=id)
#         return JsonResponse({'code': 200, 'menu': SysMenuSerializer(menu_object).data})
#
#     def delete(self, request):
#         data = json.loads(request.body.decode('utf-8'))
#         # id = request.GET.get('id')
#         id = data.get('id')
#         print(id)
#         # if SysMenu.objects.filter(parent_id=id).exists():
#         if SysMenu.objects.filter(parent_id=id).count() > 0:
#             return JsonResponse({'code': 500, 'msg': '请先删除子菜单！'})
#         else:
#             SysRoleMenu.objects.filter(menu_id=id).delete()
#             SysMenu.objects.get(id=id).delete()
#             return JsonResponse({'code': 200})
class ActionView(View):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            id = request.GET.get("id")
            if not id:
                return JsonResponse({"code": 400, "msg": '缺少必要的参数 "id"'}, status=400)

            menu_object = SysMenu.objects.get(id=id)
            return JsonResponse(
                {"code": 200, "menu": SysMenuSerializer(menu_object).data}
            )
        except SysMenu.DoesNotExist:
            return JsonResponse({"code": 404, "msg": "菜单项不存在"}, status=404)
        except Exception as e:
            return JsonResponse({"code": 500, "msg": f"服务器错误: {str(e)}"}, status=500)

    def delete(self, request):
        try:
            id = request.GET.get("id")
            if not id:
                return JsonResponse({"code": 400, "msg": '缺少必要的参数 "id"'}, status=400)

            # 检查是否有子菜单
            if SysMenu.objects.filter(parent_id=id).exists():
                return JsonResponse({"code": 500, "msg": "请先删除子菜单！"})

            # 删除关联的 SysRoleMenu 记录
            SysRoleMenu.objects.filter(menu_id=id).delete()

            # 删除 SysMenu 记录
            try:
                menu_object = SysMenu.objects.get(id=id)
                menu_object.delete()
                return JsonResponse({"code": 200, "msg": "删除成功"})
            except SysMenu.DoesNotExist:
                return JsonResponse({"code": 404, "msg": "菜单项不存在"}, status=404)
        except Exception as e:
            return JsonResponse({"code": 500, "msg": f"服务器错误: {str(e)}"}, status=500)
