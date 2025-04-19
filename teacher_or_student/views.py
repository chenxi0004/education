# from rest_framework import viewsets, permissions, status
# from rest_framework.response import Response
# from user.models import SysUser
# from role.models import SysRole, SysUserRole
# from teacher_or_student.models import Student, Teacher
# from .serializers import StudentSerializer, TeacherSerializer
#
#
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get_permissions(self):
#         # 获取当前用户的角色权限
#         user = self.request.user
#         try:
#             user_role = SysUserRole.objects.get(user=user)
#             role_code = user_role.role.code
#         except SysUserRole.DoesNotExist:
#             role_code = None
#
#         # 根据角色权限设置权限
#         if role_code in ["admin", "teacher"]:
#             return [permissions.AllowAny()]  # 允许管理员和教师访问
#         else:
#             return [permissions.IsAdminUser()]  # 其他用户无权限
#
#     def destroy(self, request, *args, **kwargs):
#         user = self.request.user
#         try:
#             user_role = SysUserRole.objects.get(user=user)
#             role_code = user_role.role.code
#         except SysUserRole.DoesNotExist:
#             role_code = None
#
#         if role_code in ["admin", "teacher"]:
#             return super().destroy(request, *args, **kwargs)
#         else:
#             return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
#
#
# class TeacherViewSet(viewsets.ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#     def get_permissions(self):
#         user = self.request.user
#         try:
#             user_role = SysUserRole.objects.get(user=user)
#             role_code = user_role.role.code
#         except SysUserRole.DoesNotExist:
#             role_code = None
#
#         if role_code == "admin":
#             return [permissions.AllowAny()]  # 只允许管理员访问
#         else:
#             return [permissions.IsAdminUser()]  # 其他用户无权限
import json

from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def list(self, request):
#         queryset = Student.objects.all()
#         serializer = StudentSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk=None):
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         student = Student.objects.get(pk=pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class TeacherViewSet(viewsets.ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#     def list(self, request):
#         queryset = Teacher.objects.all()
#         serializer = TeacherSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk=None):
#         teacher = Teacher.objects.get(pk=pk)
#         serializer = TeacherSerializer(teacher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         teacher = Teacher.objects.get(pk=pk)
#         teacher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherList(APIView):
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     teachers = Teacher.objects.all()
    #     serializer = TeacherSerializer(teachers, many=True)
    #     return Response(serializer.data)
    def get(self, request):
        query = request.GET.get('query', '')  # 获取查询参数
        if query:
            # 根据教师编号或姓名过滤数据
            teachers = Teacher.objects.filter(Q(teacher_id__icontains=query) | Q(teacher_name__icontains=query))
        else:
            teachers = Teacher.objects.all()

        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 验证请求数据
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            # 保存新资源
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 返回验证错误
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return None

    def get(self, request, pk):
        teacher = self.get_object(pk)
        if teacher is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = self.get_object(pk)
        # if teacher is None:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        if teacher is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListAllStudents(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        obj_studentList = Student.objects.all().values()  # 转成字典
        studentList = list(obj_studentList)
        return JsonResponse({"code": 200, "roleList": studentList})


class SearchView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        # data = json.loads(request.body.decode("utf-8"))
        # pageNum = data["pageNum"]
        # pageSize = data["pageSize"]
        # query = data["query"]
        query_params = request.data  # 获取 JSON 数据
        query = query_params.get('query', '')
        pageNum = int(query_params.get('pageNum', 1))
        pageSize = int(query_params.get('pageSize', 10))
        studentListPage = Paginator(
            Student.objects.filter(Q(student_name__icontains=query) | Q(student_id__icontains=query)), pageSize
        ).page(pageNum)
        obj_roles = studentListPage.object_list.values()  # 转成字典
        students = list(obj_roles)
        total = Student.objects.filter(student_id__icontains=query).count()
        return JsonResponse(
            {"code": 200, "total": total, "roleList": students, "student_id": students[0]["student_id"]})


class SaveView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        if data["student_id"] == "":  # 添加
            obj_student = Student(
                student_name=data["student_name"], gender=data["gender"],
                school=data["school"], phone_number=data["phone_number"],
            )
            obj_student.save()
        else:
            obj_student = Student(
                student_id=data["student_id"],
                student_name=data["student_name"], gender=data["gender"],
                school=data["school"], phone_number=data["phone_number"],
            )
            obj_student.save()
        return JsonResponse({"code": 200})


class ActionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        student_id = request.GET.get("student_id")
        student_object = Student.objects.get(student_id=student_id)
        return JsonResponse({"code": 200, "role": StudentSerializer(student_object).data})

    def delete(self, request):
        try:
            id = request.GET.get("student_id")
            if not id:
                return JsonResponse({"code": 400, "msg": "Missing id parameter"}, status=400)

            idList = [int(i) for i in id.split(",")]  # 将字符串转换为整数列表

            with transaction.atomic():  # 使用事务确保操作的原子性
                Student.objects.filter(student_id__in=idList).delete()

            return JsonResponse({"code": 200, "msg": "删除成功"})
        except Exception as e:
            return JsonResponse({"code": 500, "msg": f"删除失败：{str(e)}"}, status=500)


class CheckView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        name = data["student_name"]
        code = data["student_id"]
        if (
                Student.objects.filter(student_name=name).exists()
                and Student.objects.filter(student_id=code).exists()
        ):
            return JsonResponse({"code": 500})
        else:
            return JsonResponse({"code": 200})
