import json
import logging
from datetime import datetime, timezone

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse, BadHeaderError
from django.views import View
from rest_framework_simplejwt.authentication import JWTAuthentication

# from jwt.compat import constant_time_compare

from education import settings
from .models import SysUser, SysUserserializer  # 假设你的用户模型是 SysUser
from role.models import SysRole, SysUserRole
from menu.models import SysMenu, SysMenuSerializer
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone
from datetime import datetime
from django.utils.crypto import constant_time_compare
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from .models import SysUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt


#
#
# class TokenRefreshView(APIView):
#     def post(self, request):
#         refresh_token = request.data.get('refresh')
#         if not refresh_token:
#             return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             # 解析刷新令牌
#             payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
#             user_id = payload.get('user_id')
#
#             # 生成新的访问令牌
#             access_token = jwt.encode(
#                 {
#                     'user_id': user_id,
#                     'exp': payload['exp'],  # 使用相同的过期时间
#                 },
#                 settings.SECRET_KEY,
#                 algorithm='HS256'
#             )
#             return Response({'access': access_token}, status=status.HTTP_200_OK)
#         except jwt.ExpiredSignatureError:
#             return Response({'error': 'Refresh token has expired'}, status=status.HTTP_401_UNAUTHORIZED)
#         except jwt.InvalidTokenError:
#             return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)

class TokenRefreshView(APIView):

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 使用 rest_framework_simplejwt 的 RefreshToken 类
            refresh = RefreshToken(refresh_token)
            access_token = refresh.access_token
            return Response({'access': str(access_token)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


class TokenVerifyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = SysUserserializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create your views here.


class TestView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        userList_obj = SysUser.objects.all()
        userList_dict = list(userList_obj.values())
        return JsonResponse({"code": 200, "info": "测试", "data": userList_dict})


class JwtTestview(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        # user = SysUser.objects.get(username="py0", password="123456")
        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 小写快捷键ctrl+shift.+U
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # # 将用户对象传递进去，获取到该对象的属性值
        # payload = jwt_payload_handler(user)
        # # 将属性值编码成jt格式的字符串
        # token = jwt_encode_handler(payload)
        # return JsonResponse({"code": 200, "token": token})
        user = SysUser.objects.get(username="py0", password="123456")
        tokens = get_tokens_for_user(user)
        return JsonResponse({"code": 200, "token": tokens['access']})


class LoginView(APIView):
    """
    用户登录视图
    """

    def buildTreeMenu(self, sysMenuList):
        resultMenuList: list[SysMenu] = list()
        for menu in sysMenuList:
            # 寻找子节点
            for e in sysMenuList:
                if e.parent_id == menu.id:
                    if not hasattr(menu, "children"):
                        menu.children = list()
                    menu.children.append(e)
            # 判断父节点，添加到集合
            if menu.parent_id == 0:
                resultMenuList.append(menu)

        return resultMenuList

    def post(self, request):
        username = request.GET.get("username")
        password = request.GET.get("password")
        # try:
        #     # 从数据库中获取用户
        #     user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     return False  # 用户不存在
        #
        #     # 验证密码
        # if bcrypt.checkpw(password.encode('utf-8'), user.password):
        #     return True  # 密码正确
        # else:
        #     return False  # 密码错误
        try:
            user = SysUser.objects.get(username=username, password=password)
            # 检查用户是否存在
            if user is None:
                return Response({"code": 401, "info": "用户名或密码错误"}, status=status.HTTP_401_UNAUTHORIZED)
            if user.status == 0:
                return Response({"code": 402, "info": "用户被禁用"}, status=status.HTTP_402_PAYMENT_REQUIRED)
            # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 小写快捷键ctrl+shift.+U
            # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            # # 将用户对象传递进去，获取到该对象的属性值
            # payload = jwt_payload_handler(user)
            # # 将属性值编码成jt格式的字符串
            # token = jwt_encode_handler(payload)
            tokens = get_tokens_for_user(user)
            token = tokens['access']
            refresh = tokens['refresh']
            roleList = SysRole.objects.raw(
                "SELECT id,name FROM sys_role where id IN (SELECT role_id FROM sys_user_role where user_id="
                + str(user.id)
                + ")"
            )
            # 获取当前用户角色
            roles = ",".join([role.name for role in roleList])
            menuSet: set[SysMenu] = set()
            for row in roleList:
                menuList = SysMenu.objects.raw(
                    "SELECT * FROM sys_menu where id IN (SELECT menu_id FROM sys_role_menu where role_id="
                    + str(row.id)
                    + ")"
                )
                for row2 in menuList:
                    # print(row2.id, row2.name)
                    menuSet.add(row2)
            menuList: list[SysMenu] = list(menuSet)
            sorted_menuList = sorted(
                menuList, key=lambda x: x.order_num
            )  # 根据order_num排序
            # 构造菜单树
            sysMenuList: list[SysMenu] = self.buildTreeMenu(sorted_menuList)
            serializerMenuList = list()
            for sysMenu in sysMenuList:
                serializerMenuList.append(SysMenuSerializer(sysMenu).data)
            # serializerMenuList = [SysMenuSerializer(sysMenu).data for sysMenu in sysMenuList]
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, "info": "用户名或者密码错误!"})
        return JsonResponse(
            {
                "code": 200,
                "token": token,
                "refresh": refresh,  # 返回refresh令牌
                "user": SysUserserializer(user).data,
                "info": "登录成功！",
                "roles": roles,
                "menuList": serializerMenuList,
            }
        )


# class RegisterView(View):
#     def post(self, request):
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirmPassword")
#         if not username or not password or not confirm_password:
#             return JsonResponse({"code": 400, "info": "用户名和密码不能为空"})
#         if password != confirm_password:
#             return JsonResponse({"code": 400, "info": "两次输入的密码不一致"})
#         try:
#             SysUser.objects.get(username=username)
#             return JsonResponse({"code": 400, "info": "用户名已存在"})
#         except SysUser.DoesNotExist:
#             pass
#
#         user = SysUser(
#             username=username,
#             # password=make_password(password)##使用哈希方法转换密码
#             # make_password,check_password
#             password=password,
#         )
#         user.save()
#
#         return JsonResponse({"code": 200, "info": "注册成功"})


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.signing import TimestampSigner


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # 使用 PasswordResetTokenGenerator 的默认逻辑
        return super()._make_hash_value(user, timestamp)


token_generator = AccountActivationTokenGenerator()


def generate_activation_token(user):
    signer = TimestampSigner()
    token = signer.sign(token_generator.make_token(user))
    return token


def verify_activation_token(user, token):
    signer = TimestampSigner()
    try:
        # 验证时间戳
        original_token = signer.unsign(token, max_age=3600)  # 令牌有效期为 1 小时
        return token_generator.check_token(user, original_token)
    except SignatureExpired:
        return False
    except BadSignature:
        return False


class RegisterView(APIView):
    permission_classes = []  # 注册接口不需要认证

    def post(self, request):
        data = request.data
        username = data.get("username")
        password = data.get("password")
        confirm_password = data.get("confirmPassword")
        email = data.get("email")

        if not username or not password or not confirm_password or not email:
            return Response({"code": 400, "info": "用户名、密码、确认密码和邮箱不能为空"},
                            status=status.HTTP_400_BAD_REQUEST)
        if password != confirm_password:
            return Response({"code": 400, "info": "两次输入的密码不一致"}, status=status.HTTP_400_BAD_REQUEST)

        if SysUser.objects.filter(username=username).exists():
            return Response({"code": 400, "info": "用户名已存在"}, status=status.HTTP_400_BAD_REQUEST)
        if SysUser.objects.filter(email=email).exists():
            return Response({"code": 400, "info": "邮箱已被注册"}, status=status.HTTP_400_BAD_REQUEST)
        # # 对密码进行哈希处理
        # salt = bcrypt.gensalt()  # 生成盐值
        # hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        #
        # # 将用户名和哈希密码存储到数据库
        user = SysUser(
            username=username,
            email=email,
            password=password,
            # status=False  # 注册后用户默认未激活
        )
        # user.set_password(password)
        # user.status=True
        user.save()

        token = generate_activation_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        activation_link = f"{settings.DOMAIN}/activate/{uid}/{token}"

        message = "\n".join([
            f"欢迎注册, {username}!",
            "请访问以下链接完成用户激活:",
            activation_link
        ])

        try:
            send_mail(
                "用户激活邮件",
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
        except Exception as e:
            return Response({"code": 500, "info": f"邮件发送失败: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"code": 200, "info": "注册成功，请登录邮箱激活账号"}, status=status.HTTP_200_OK)


class active_user(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = SysUser.objects.get(id=uid)
        except (TypeError, ValueError, OverflowError, SysUser.DoesNotExist):
            return JsonResponse({"success": False, "message": "无效的激活链接"})

        if verify_activation_token(user, token):
            user.status = True
            user.save()
            return JsonResponse({"success": True, "message": "账号激活成功"})
        else:
            return JsonResponse({"success": False, "message": "激活链接已过期或无效"})


class SaveView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        # serializer = SysUserserializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        if data["id"] == -1:
            obj_sysUser = SysUser(
                username=data["username"],
                password=data["password"],
                email=data["email"],
                phonenumber=data["phonenumber"],
                status=data["status"],
                remark=data["remark"],
                student_or_teacher_id=data["student_or_teacher_id"],
            )
            obj_sysUser.create_time = datetime.now().date()
            obj_sysUser.avatar = "default.jpg"
            obj_sysUser.password = "123456"
            obj_sysUser.save()
        else:
            obj_sysUser = SysUser(
                id=data["id"],
                username=data["username"],
                password=data["password"],
                avatar=data["avatar"],
                email=data["email"],
                phonenumber=data["phonenumber"],
                login_date=data["login_date"],
                status=data["status"],
                create_time=data["create_time"],
                update_time=data["update_time"],
                remark=data["remark"],
                gender=data["gender"],
                student_or_teacher_id=data["student_or_teacher_id"],
            )
            obj_sysUser.update_time = datetime.now().date()
            obj_sysUser.save()
        return JsonResponse({"code": 200, 'msg': '操作成功！'})


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class PwdView(APIView):
    permission_classes = (IsAuthenticated,)

    # permission_classes = [IsAuthenticated]

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        id = data["id"]
        oldPassword = data["oldPassword"]
        newPassword = data["newPassword"]
        obj_user = SysUser.objects.get(id=id)
        if obj_user.password == oldPassword:
            # obj_user.update_password(newPassword)
            obj_user.password = newPassword
            obj_user.update_time = datetime.now().date()
            obj_user.save()
            return JsonResponse({"code": 200})
        else:
            return JsonResponse({"code": 500, "errorInfo": "原密码输入错误！"})


class ImageView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        file = request.FILES.get("avatar")
        print("filename", file)
        if file:
            file_name = file.name
            # suffixName=file_name[file_name.rfind('.')+1:]
            suffixName = file_name[file_name.rfind("."):]
            new_file_name = datetime.now().strftime("%Y%m%d%H%M%S") + suffixName
            file_path = str(settings.MEDIA_ROOT) + "\\userAvatar\\" + new_file_name
            # file_path = os.path.join(settings.MEDIA_ROOT, "userAvatar", new_file_name)  # 使用 os.path.join 构建路径
            try:
                with open(file_path, "wb") as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                return JsonResponse({"code": 200, "title": new_file_name})
            except:
                return JsonResponse({"code": 500, "errorInfo": "上传头像失败！"})


class AvatarView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        id = data["id"]
        avatar = data["avatar"]
        obj_user = SysUser.objects.get(id=id)
        obj_user.avatar = avatar
        obj_user.save()
        return JsonResponse({"code": 200})


class SearchView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        pageNum = data["pageNum"]
        pageSize = data["pageSize"]
        query = data["query"]
        # userListPage = Paginator(SysUser.objects.filter(username__icontains=query).order_by('username'), pageSize).page(pageNum)
        userListPage = Paginator(
            SysUser.objects.filter(Q(username__icontains=query) | Q(student_or_teacher_id__icontains=query)), pageSize
        ).page(pageNum)
        obj_users = userListPage.object_list.values()  # 转成字典
        users = list(obj_users)
        for user in users:
            userId = user["id"]
            roleList = SysRole.objects.raw(
                "SELECT id,name FROM sys_role where id IN (SELECT role_id FROM sys_user_role where user_id="
                + str(userId)
                + ")"
            )
            roleListDict = []
            for role in roleList:
                roleDict = {}
                roleDict["id"] = role.id
                roleDict["name"] = role.name
                roleListDict.append(roleDict)
            user["roleList"] = roleListDict
        total = SysUser.objects.filter(username__icontains=query).count()
        return JsonResponse({"code": 200, "total": total, "users": users})


# from django.db.models import Value, CharField
# from django.db.models.functions import Coalesce
#
# class SearchView(View):
#     def post(self, request):
#         data = request.data
#         pageNum = data.get("pageNum")
#         pageSize = data.get("pageSize")
#         query = data.get("query")
#
#         users = SysUser.objects.filter(
#             Q(username__icontains=query) | Q(student_or_teacher_id__icontains=query)
#         ).annotate(
#             role_list=Coalesce(
#                 Value(""),
#                 Value(", ".join([role.name for role in SysRole.objects.filter(sysuserrole__user_id=OuterRef("id"))])),
#                 output_field=CharField()
#             )
#         ).values("id", "username", "email", "role_list")
#
#         paginator = Paginator(users, pageSize)
#         page = paginator.page(pageNum)
#
#         return JsonResponse({
#             "code": 200,
#             "total": paginator.count,
#             "users": list(page.object_list)
#         })

class ActionView(View):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.GET.get("id")
        user_object = SysUser.objects.get(id=id)
        return JsonResponse({"code": 200, "user": SysUserserializer(user_object).data})

    # def delete(self, request):
    #     idList = json.loads(request.body.decode('utf-8'))
    #     SysUserRole.objects.filter(user_id__in=idList).delete()
    #     SysUser.objects.filter(id__in=idList).delete()
    #     return JsonResponse({'code': 200})
    def delete(self, request):
        id = request.GET.get("id")
        if not id:
            return JsonResponse(
                {"code": 400, "msg": "Missing id parameter"}, status=400
            )

        idList = [int(i) for i in id.split(",")]  # 将字符串转换为整数列表
        SysUserRole.objects.filter(user_id__in=idList).delete()
        SysUser.objects.filter(id__in=idList).delete()
        return JsonResponse({"code": 200})


class CheckView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        username = data["username"]
        if SysUser.objects.filter(username=username).exists():
            return JsonResponse({"code": 500})
        else:
            return JsonResponse({"code": 200})


class PasswordView(View):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.GET.get("id")
        user_object = SysUser.objects.get(id=id)
        user_object.password = "123456"
        user_object.update_time = datetime.now().date()
        user_object.save()
        return JsonResponse({"code": 200})


class StatusView(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        id = data["id"]
        status = data["status"]
        user_object = SysUser.objects.get(id=id)
        user_object.status = status
        user_object.update_time = datetime.now().date()
        user_object.save()
        return JsonResponse({"code": 200})


# 用户角色授权
class GrantRole(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            user_id = data["id"]
            role_ids = data["roleIds"]

            # 删除用户的所有角色关联
            SysUserRole.objects.filter(user_id=user_id).delete()

            # 添加新的角色关联
            for role_id in role_ids:
                userRole = SysUserRole(user_id=user_id, role_id=role_id)
                userRole.update_time = datetime.now().date()
                userRole.save()

            return JsonResponse({"code": 200, "msg": "操作成功"})
        except Exception as e:
            return JsonResponse({"code": 500, "msg": str(e)}, status=500)


from django.views.decorators.csrf import csrf_exempt
from django.db import transaction


# @csrf_exempt
class Batch_grant_role(View):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # try:
        #     data = json.loads(request.body.decode("utf-8"))
        #     user_ids = data.get("userIds")
        #     role_ids = data.get("roleIds")
        #     if not user_ids or not role_ids:
        #         return JsonResponse({"code": 400, "msg": "用户ID或角色ID不能为空"})
        #
        #     with transaction.atomic():  # 使用事务确保操作的原子性
        #         # for user_id in user_ids:
        #         #     SysUserRole.objects.filter(user_id=user_id).delete()  # 清除用户现有的角色
        #         #     for role_id in role_ids:
        #         #         user_role = SysUserRole(user_id=user_id, role_id=role_id)
        #         #         user_role.update_time = datetime.now()
        #         #         user_role.save()
        #         # 批量删除用户现有的角色
        #         SysUserRole.objects.filter(user_id__in=user_ids).delete()
        #
        #         # 批量创建新的用户角色关系
        #         user_roles_to_create = [
        #             SysUserRole(user_id=user_id, role_id=role_id, update_time=datetime.now())
        #             for user_id in user_ids
        #             for role_id in role_ids
        #         ]
        #         SysUserRole.objects.bulk_create(user_roles_to_create)
        #
        #     return JsonResponse({"code": 200, "msg": "角色分配成功"})
        # except SysUser.DoesNotExist:
        #     return JsonResponse({"code": 404, "msg": "用户不存在"})
        # except SysRole.DoesNotExist:
        #     return JsonResponse({"code": 404, "msg": "角色不存在"})
        # except Exception as e:
        #     return JsonResponse({"code": 500, "msg": f"服务器错误: {str(e)}"})
        logger = logging.getLogger(__name__)

        try:
            data = json.loads(request.body.decode("utf-8"))
            user_ids = data.get("userIds")
            role_ids = data.get("roleIds")
            print(user_ids, role_ids)
            if not user_ids or not role_ids:
                return JsonResponse({"code": 400, "msg": "用户ID或角色ID不能为空"})
            with transaction.atomic():
                # 删除现有角色关系
                SysUserRole.objects.filter(user_id__in=user_ids).delete()

                # 创建新的用户角色关系
                user_roles_to_create = [
                    SysUserRole(user_id=user_id, role_id=role_id)
                    for user_id in user_ids
                    for role_id in role_ids
                ]
                SysUserRole.objects.bulk_create(user_roles_to_create)
            return JsonResponse({"code": 200, "info": "用户角色更新成功"})
            # logger.info("用户角色更新成功")
        except Exception as e:
            logger.error(f"用户角色更新失败: {e}")
