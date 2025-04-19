import json
from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from rest_framework.permissions import IsAuthenticated

from menu.models import SysRoleMenu
from .models import SysRole, SysUserRole, SysRoleSerializer
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse
from django.db import transaction


# Create your views here.
class ListAllView(View):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        obj_roleList = SysRole.objects.all().values()  # 转成字典
        roleList = list(obj_roleList)
        return JsonResponse({"code": 200, "roleList": roleList})


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework import status
# class ListAllView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#
#     def get(self, request):
#         obj_roleList = SysRole.objects.all().values()
#         roleList = list(obj_roleList)
#         return Response({"code": 200, "roleList": roleList}, status=status.HTTP_200_OK)


class SearchView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        pageNum = data["pageNum"]
        pageSize = data["pageSize"]
        query = data["query"]
        # roleListPage = Paginator(SysRole.objects.filter(name__icontains=query).order_by('name'), pageSize).page(pageNum)
        roleListPage = Paginator(
            SysRole.objects.filter(name__icontains=query), pageSize
        ).page(pageNum)
        obj_roles = roleListPage.object_list.values()  # 转成字典
        roles = list(obj_roles)
        total = SysRole.objects.filter(name__icontains=query).count()
        return JsonResponse({"code": 200, "total": total, "roleList": roles})


class SaveView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        # print(data)
        if data["id"] == -1:  # 添加
            obj_sysRole = SysRole(
                name=data["name"], code=data["code"], remark=data["remark"]
            )
            obj_sysRole.create_time = datetime.now().date()
            obj_sysRole.save()
        else:
            obj_sysRole = SysRole(
                id=data["id"],
                name=data["name"],
                code=data["code"],
                remark=data["remark"],
                create_time=data["create_time"],
                update_time=data["update_time"],
            )
            obj_sysRole.update_time = datetime.now().date()
            obj_sysRole.save()
        return JsonResponse({"code": 200})


# from django.core.exceptions import ValidationError
# class SaveView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             if not data['name'] or not data['code']:
#                 return JsonResponse({'code': 400, 'msg': '角色名和权限字符不能为空'})
#             if data['id'] == -1:  # 添加
#                 obj_sysRole = SysRole(
#                     name=data['name'],
#                     code=data['code'],
#                     remark=data['remark'],
#                     create_time=datetime.now().date()
#                 )
#             else:  # 更新
#                 obj_sysRole = SysRole.objects.get(id=data['id'])
#                 obj_sysRole.name = data['name']
#                 obj_sysRole.code = data['code']
#                 obj_sysRole.remark = data['remark']
#                 obj_sysRole.update_time = datetime.now().date()
#             obj_sysRole.full_clean()  # 验证模型字段
#             obj_sysRole.save()
#             return JsonResponse({'code': 200})
#         except ValidationError as e:
#             return JsonResponse({'code': 400, 'msg': e.message_dict})
#         except Exception as e:
#             logger.error(f"SaveView error: {e}")
#             return JsonResponse({'code': 500, 'msg': '服务器错误'})


class ActionView(View):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.GET.get("id")
        role_object = SysRole.objects.get(id=id)
        return JsonResponse({"code": 200, "role": SysRoleSerializer(role_object).data})

    def delete(self, request):
        try:
            id = request.GET.get("id")
            if not id:
                return JsonResponse({"code": 400, "msg": "Missing id parameter"}, status=400)

            idList = [int(i) for i in id.split(",")]  # 将字符串转换为整数列表

            with transaction.atomic():  # 使用事务确保操作的原子性
                SysUserRole.objects.filter(role_id__in=idList).delete()
                SysRoleMenu.objects.filter(role_id__in=idList).delete()
                SysRole.objects.filter(id__in=idList).delete()

            return JsonResponse({"code": 200, "msg": "删除成功"})
        except Exception as e:
            return JsonResponse({"code": 500, "msg": f"删除失败：{str(e)}"}, status=500)


class CheckView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        name = data["name"]
        code = data["code"]
        if (
                SysRole.objects.filter(name=name).exists()
                or SysRole.objects.filter(code=code).exists()
        ):
            return JsonResponse({"code": 500})
        else:
            return JsonResponse({"code": 200})


class MenusView(View):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.GET.get("id")
        menuList = SysRoleMenu.objects.filter(role_id=id).values("menu_id")
        menuIdList = [m["menu_id"] for m in menuList]
        return JsonResponse({"code": 200, "menuIdList": menuIdList})


# 角色授权
class GrantView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        role_id = data["id"]
        menuIdList = data["menuIds"]
        SysRoleMenu.objects.filter(role_id=role_id).delete()
        for menuId in menuIdList:
            # SysRoleMenu.objects.create(role_id=role_id, menu_id=menuId)
            roleMenu = SysRoleMenu(role_id=role_id, menu_id=menuId)
            roleMenu.save()
        return JsonResponse({"code": 200})

# class GrantView(View):
#     def post(self, request):
#         data = json.loads(request.body.decode('utf-8'))
#         role_id = data['id']
#         menuIdList = data['menuIds']
#         if not menuIdList:
#             return JsonResponse({'code': 400, 'msg': '至少需要分配一个菜单权限'})
#         SysRoleMenu.objects.filter(role_id=role_id).delete()
#         for menuId in menuIdList:
#             SysRoleMenu.objects.create(role_id=role_id, menu_id=menuId)
#         return JsonResponse({'code': 200})
