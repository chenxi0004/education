# from django.shortcuts import render
#
# # Create your views here.
# import requests
#
# def get_student(student_id):
#     response = requests.get(f"http://user-management-project-url/api/students/{student_id}/")
#     if response.status_code == 200:
#         return response.json()
#     return None
#
#
# # 课程管理服务的权限逻辑
# def has_permission(user, permission_code):
#     # 假设通过 API 获取用户的角色权限代码
#     user_role_code = get_user_role_code(user.username)
#     return permission_code in user_role_code
#
# def get_user_role_code(username):
#     response = requests.get(f"http://user-management-project-url/api/users/{username}/")
#     if response.status_code == 200:
#         return response.json().get("role_code")
#     return None
#
#
# # 课程管理服务的 views.py
# from rest_framework import viewsets
# from .models import Student
# from .serializers import StudentSerializer
#
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get_permissions(self):
#         # 只有教师角色可以对学生表进行操作
#         if self.request.user.role_code == "teacher":
#             return [permission() for permission in self.permission_classes]
#         return []
import json

from django.db import transaction
from django.db.models import Q, Sum
from django.db.models.functions import TruncDate
from django.http import JsonResponse
from django.db.models import Case, When, Value, BooleanField
# course_management_project/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Course
# from .utils import get_student, get_teacher
#
#
# # class CourseDetailView(APIView):
# #     def get(self, request, course_id):
# #         course = Course.objects.get(course_id=course_id)
# #         teacher_data = get_teacher(course.teacher_id)
# #         student_data = [get_student(enrollment.student_id) for enrollment in course.enrollment_set.all()]
# #
# #         return Response({
# #             'course_name': course.course_name,
# #             'teacher': teacher_data,
# #             'students': student_data
# #         })
#
#
# # course_management_project/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Course, Enrollment
# from .utils import get_student, get_teacher
#
# class CourseDetailView(APIView):
#     def get(self, request, course_id):
#         # # 从请求头中获取 Token
#         # token = request.headers.get('Authorization')
#         try:
#             # 获取课程对象
#             course = Course.objects.get(course_id=course_id)
#         except Course.DoesNotExist:
#             return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         # 获取教师信息
#         # teacher_data = get_teacher(course.teacher_id, token)
#         teacher_data = get_teacher(course.teacher_id)
#         if not teacher_data:
#             return Response({'error': 'Teacher data not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         # 获取选课的学生信息
#         student_data = []
#         for enrollment in Enrollment.objects.filter(course=course):
#             # student_info = get_student(enrollment.student_id, token)
#             student_info = get_student(enrollment.student_id)
#             if student_info:
#                 student_data.append(student_info)
#
#         # 构建响应数据
#         response_data = {
#             'course_id': course.course_id,
#             'course_name': course.course_name,
#             'teacher': teacher_data,
#             'students': student_data
#         }
#
#         return Response(response_data, status=status.HTTP_200_OK)


# course_management/views.py
from rest_framework import viewsets, permissions, status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from course_material.models import Material, Video
from .models import Course, Enrollment, Grade,LearningProgress,LearningRecord,Chapter
from .serializers import CourseSerializer, EnrollmentSerializer, GradeSerializer, LearningProgressSerializer, LearningRecordSerializer, ChapterSerializer
# from .permissions import IsTeacher, IsStudent
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
import requests
from rest_framework.permissions import AllowAny

from .utils import get_teacher, get_student
from django.db import models

class VerifyTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get('token')
        response = requests.post('http://localhost:8000/user/verify/', headers={'Authorization': f'Bearer {token}'})
        if response.status_code == 200:
            return Response(response.json(), status=response.status_code)
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # def get_queryset(self):
    #     userid = self.request.user.student_or_teacher_id
    #     # 返回当前教师创建的课程
    #     return Course.objects.filter(teacher_id=userid)
    def get_queryset(self):
        # 获取请求参数中的 teacher_id
        teacher_id = self.request.GET.get('teacher_id')
        if teacher_id:
            # 如果提供了 teacher_id，只返回该教师创建的课程
            return Course.objects.filter(teacher_id=teacher_id)
        course_ids = self.request.GET.get('course_id__in')
        if course_ids:
            # 如果提供了 course_id__in，只返回指定的课程
            course_id_list = course_ids.split(',')
            return Course.objects.filter(course_id__in=course_id_list)
        return super().get_queryset()

    def perform_create(self, serializer):

        course_cover = self.request.FILES.get('course_cover')
        serializer.save(course_cover=course_cover)

    def perform_update(self, serializer):
        instance = self.get_object()
        course_cover = self.request.FILES.get('course_cover')
        if course_cover:
            instance.course_cover = course_cover
            instance.save()
        serializer.save()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if instance.teacher_id != request.user.student_or_teacher_id:
    #         raise PermissionDenied("You do not have permission to delete this course")
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            return Chapter.objects.filter(course_id=course_id)
        return super().get_queryset()


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    # permission_classes = (IsAuthenticated,)
    permission_classes = []  # 禁用权限验证
    # def get_permissions(self):
    #     if self.action in ["create", "update", "destroy"]:
    #         return [permissions.IsAuthenticated(), IsTeacher()]
    #     return super().get_permissions()

class CourseDetailView(APIView):
    # permission_classes = [IsAuthenticated]  # 确保权限类正确
    # permission_classes = []  # 禁用权限验证
    # from django.core.cache import cache
    # # 清理所有缓存
    # cache.clear()
    def get(self, request, course_id):
        try:
            course = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        # try:
        #     # 获取当前登录的教师编号
        #     teacher_id = request.user.teacher_id
        #     # 确保课程是由当前教师创建的
        #     course = Course.objects.get(course_id=course_id, teacher_id=teacher_id)
        # except Course.DoesNotExist:
        #     return Response({'error': 'Course not found or you do not have permission to view this course'},
        #                     status=status.HTTP_404_NOT_FOUND)
        teacher_data = get_teacher(course.teacher_id)
        student_data = [get_student(enrollment.student_id) for enrollment in Enrollment.objects.filter(course=course)]
        response_data = {
            'course_id': course.course_id,
            'course_name': course.course_name,
            'course_cover': course.course_cover.url if course.course_cover else None,  # 返回封面 URL
            # 'course_cover': request.build_absolute_uri(course.course_cover.url) if course.course_cover else None,
            # 返回完整的 URL
            'course_intro': course.course_intro,
            'course_type': course.course_type,
            'teacher_id': course.teacher_id,
            'teacher': teacher_data,
            'students': student_data,
            'start_time': course.start_time,
            'end_time': course.end_time
        }

        return Response(response_data, status=status.HTTP_200_OK)

class CourseSearchView(APIView):
    def get(self, request):
        # 获取查询参数
        query = request.GET.get('query', '')  # 使用 request.GET 获取查询参数
        teacher_id = request.GET.get('student_or_teacher_id', '')  # 获取教师编号
        if teacher_id==None:
            teacher_id = request.GET.get('teacher_id', '')  # 教师编号


        # 构建查询条件
        if teacher_id:
            # 如果提供了教师编号，查询该教师创建的课程
            courses = Course.objects.filter(teacher_id=teacher_id)
        else:
            # 否则，根据课程名称或课程编号进行搜索
            courses = Course.objects.filter(
                Q(course_name__icontains=query) | Q(course_id__icontains=query)
            )

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentEnrollmentView(APIView):
    def post(self, request, course_id):
        # 从表单数据中获取用户名
        # data = json.loads(request.body.decode("utf-8"))
        # userid = data.get("userid")
        userid = request.data.get("userid")
        if not userid:
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)

        # 查询参数
        query_params = {
            'query': userid,  # 查询关键词
            'pageNum': 1,  # 当前页码
            'pageSize': 10  # 每页显示的条数
        }

        # 调用函数获取学生信息
        student_id = get_student(query_params)
        # 从用户管理系统获取学生编号
        # student_id = get_student(userid)
        if not student_id:
            return Response({"error": "Student ID not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            course = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        if Enrollment.objects.filter(student_id=student_id, course_id=course).exists():
            return Response({"error": "You have already enrolled in this course"}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():##确保事务操作原子性
            Enrollment.objects.create(student_id=student_id, course_id=course)
            # 检查是否已经存在 LearningProgress 记录
            if not LearningProgress.objects.filter(student_id=student_id, course_id=course).exists():
                # 如果不存在，则创建 LearningProgress 记录
                LearningProgress.objects.create(student_id=student_id, course_id=course)

            # 获取已选课程列表
            enrolled_courses = Enrollment.objects.filter(student_id=userid).values_list('course_id', flat=True)

        return Response({
            "message": "Enrollment successful",
            "enrolled_courses": list(enrolled_courses)
        }, status=status.HTTP_201_CREATED)



class StudentEnrollmentListView(APIView):
    def get(self, request, course_id):
        userid = request.data.get('userid')
        if not userid:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        enrollmentlist = Enrollment.objects.all().values()  # 转成字典
        enrollmentList = list(enrollmentlist)
        return JsonResponse({"code": 200, "enrollmentList": enrollmentList})
class EnrolledCoursesView(APIView):
    def get(self, request):
        student_id = request.GET.get('student_id')
        if not student_id:
            return Response({"error": "Student ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        enrolled_courses = Enrollment.objects.filter(student_id=student_id).values_list('course_id', flat=True)
        return Response(list(enrolled_courses), status=status.HTTP_200_OK)

class StudentUnenrollmentView(APIView):
    def delete(self, request, course_id):
        userid = request.data.get("userid")
        if not userid:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            course = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        enrollment = Enrollment.objects.filter(student_id=userid, course_id=course)
        if not enrollment.exists():
            return Response({"error": "You are not enrolled in this course"}, status=status.HTTP_400_BAD_REQUEST)
        enrollment.delete()
        LearningProgress.objects.filter(student_id=userid, course_id=course).delete()

        return Response({"message": "Unenrollment successful"}, status=status.HTTP_200_OK)

# class CourseSearchView(APIView):
#     def get(self, request):
#         query = request.data.get('query', '')  # 搜索关键词
#         student_or_teacher_id = request.data.get('student_or_teacher_id', '')  # 用户 ID
#
#         courses = Course.objects.filter(
#             Q(course_name__icontains=query) | Q(course_id__icontains=query)
#         )
#
#         if student_or_teacher_id:
#             # 获取用户已报名的课程 ID 列表
#             enrolled_courses = Enrollment.objects.filter(student_id=student_or_teacher_id).values_list('course_id', flat=True)
#             # 动态添加 enrolled 字段，表示用户是否已报名该课程
#             courses = courses.annotate(enrolled=Case(
#                 When(course_id__in=enrolled_courses, then=Value(True)),
#                 default=Value(False),
#                 output_field=BooleanField()
#             ))
#
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)




class StudentCourseVideosView(APIView):
    def get(self, request, student_id, course_id):
        # 检查学生是否选了这门课程
        try:
            enrollment = Enrollment.objects.get(student_id=student_id, course_id=course_id)
        except Enrollment.DoesNotExist:
            return Response({"error": "You are not enrolled in this course"}, status=status.HTTP_403_FORBIDDEN)

        # 获取课程下的所有视频
        videos = Video.objects.filter(course_id=course_id, review_status='approved')  # 只返回审核通过的视频
        video_data = [
            {
                "video_id": video.video_id,
                "video_name": video.video_name,
                "video_url": video.video_file.url,  # 假设 Video 模型有一个 `video_file` 字段
                "review_status": video.review_status
            }
            for video in videos
        ]

        return Response({"videos": video_data}, status=status.HTTP_200_OK)




class LearningProgressView(APIView):

    # def get(self, request, course_id,student_id):
    def patch(self, request, course_id, student_id):
        try:
            progress = LearningProgress.objects.get(student_id=student_id, course_id=course_id)
        except LearningProgress.DoesNotExist:
            return Response({"error": "Progress not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LearningProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LearningRecordView(APIView):

    def post(self, request):
        student_id = request.data.get("student_id")  # 从请求体中获取 student_id
        course_id = request.data.get("course_id")  # 从请求体中获取 course_id
        content = request.data.get("content")
        duration = request.data.get("duration")
        # material_id = request.data.get("material_id")  # 获取学习的视频资料编号
        video_id = request.data.get("video_id")
        is_completed = request.data.get("is_completed")

        # if not content or not duration or not material_id or not video_id:
        if not content or not video_id:
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(course_id=course_id)
        except (Course.DoesNotExist, Material.DoesNotExist):
            return Response({"error": "Course  not found"}, status=status.HTTP_404_NOT_FOUND)
        # try:
        #     material = Material.objects.get(material_id=material_id, course_id=course, status='approved')  # 确保视频已审核通过
        # except Material.DoesNotExist:
        #     return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            video = Video.objects.get(video_id=video_id, course_id=course, review_status='approved')  # 确保视频已审核通过
        except Video.DoesNotExist:
            return Response({"error": "Video not found"}, status=status.HTTP_404_NOT_FOUND)

        # 检查是否已完播
        if is_completed:
            # 如果已完播，不再累计时长
            if LearningRecord.objects.filter(student_id=student_id, video_id=video_id, is_completed=True).exists():
                return Response({"message": "Video already completed"}, status=status.HTTP_200_OK)

        record = LearningRecord.objects.create(
            student_id=student_id,
            course_id=course,
            # material_id=material,
            video_id=video,
            content=content,
            duration=duration,
            is_completed=is_completed
        )

        # # 计算已观看视频的总时长
        # watched_duration = LearningRecord.objects.filter(student_id=student_id, course_id=course).aggregate(
        #     total_duration=models.Sum('duration'))['total_duration'] or 0
        # # 计算学习进度
        progress, created = LearningProgress.objects.get_or_create(student_id=student_id, course_id=course_id)
        completed_videos = LearningRecord.objects.filter(student_id=student_id, course_id=course_id, is_completed=True)
        total_completed_duration = sum(record.video_id.video_duration for record in completed_videos)
        progress.progress = (total_completed_duration / course.total_video_duration) * 100
        progress.progress = min(progress.progress, 100)  # 限制进度不超过 100%
        progress.save()


        # progress, _ = LearningProgress.objects.get_or_create(student_id=student_id, course_id=course)
        # progress.progress=progress.progress + (duration / course.total_video_duration) * 100 if course.total_video_duration > 0 else 0
        # progress.progress=progress.progress if progress.progress<=100 else 100
        # progress.save()

        serializer = LearningRecordSerializer(record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LearningReportView(APIView):
    def get(self, request, student_id):
        # try:
        #     student_name = get_student(student_id)["student_name"]
        # except Exception as e:
        #     return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        enrollments = Enrollment.objects.filter(student_id=student_id)
        report = []

        for enrollment in enrollments:
            course = enrollment.course_id
            progress = LearningProgress.objects.get(student_id=student_id, course_id=course)
            records = LearningRecord.objects.filter(student_id=student_id, course_id=course).order_by('record_time')

            # 计算总学习时长
            # total_duration = records.aggregate(total_duration=Sum('duration'))['total_duration'] or 0
            # # 获取每次学习的日期与时间统计
            # learning_sessions = records.values('record_time', 'duration')
            # 按日期分组统计每天的学习时间
            daily_durations = records.annotate(date=TruncDate('record_time')).values('date').annotate(
                daily_duration=Sum('duration')).order_by('date')
            # 获取学习内容统计
            content_summary = records.values('content').annotate(total_duration=Sum('duration'))

            course_report = {
                "course_id": course.course_id,
                "course_name": course.course_name,
                "progress": progress.progress,
                "total_duration": sum(record.duration for record in records),
                # "learning_sessions": list(learning_sessions),
                "daily_durations": list(daily_durations),
                "content_summary": list(content_summary),
                "records": LearningRecordSerializer(records, many=True).data
            }
            report.append(course_report)

        return Response({
            "student_id": student_id,
            # "student_name": student_name,
            "report": report
        }, status=status.HTTP_200_OK)


from rest_framework import generics
from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Exam,Question,ExamSubmission
from .serializers import ExamSerializer,QuestionSerializer,ExamSubmissionSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            return Exam.objects.filter(course_id=course_id)
        return super().get_queryset()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        exam_id = self.request.GET.get('exam_id')
        if exam_id:
            return Question.objects.filter(exam_id=exam_id)
        return super().get_queryset()


class ExamSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ExamSubmission.objects.all()
    serializer_class = ExamSubmissionSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student_id = self.request.GET.get('student_id')
        if student_id:
            return ExamSubmission.objects.filter(student_id=student_id)
        return super().get_queryset()


class TeacherExamManagementView(APIView):
    """教师考试管理"""

    def post(self, request):
        """创建考试"""
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            exam = serializer.save()
            return Response(ExamSerializer(exam).data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, exam_id):
        """更新考试信息"""
        exam = get_object_or_404(Exam, exam_id=exam_id)
        serializer = ExamSerializer(exam, data=request.data, partial=True)
        # 支持批量题目操作
        if 'questions' in request.data:
            Question.objects.filter(exam_id=exam_id).delete()
            for q_data in request.data['questions']:
                Question.objects.create(exam_id=exam, **q_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TeacherQuestionManagementView(APIView):
    """教师题目管理"""

    def post(self, request, exam_id):
        """添加题目"""
        exam = get_object_or_404(Exam, exam_id=exam_id)
        request.data['exam_id'] = exam_id
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, question_id):
        """更新题目"""
        question = get_object_or_404(Question, question_id=question_id)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TeacherExamPublishView(APIView):
    """发布考试"""

    def post(self, request, exam_id):
        exam = get_object_or_404(Exam, exam_id=exam_id)
        if Question.objects.filter(exam_id=exam_id).count() == 0:
            return Response({"error": "考试没有题目，无法发布"}, status=400)

        exam.is_published = True
        exam.save()
        # 创建题目
        questions = request.data.get('questions', [])
        for q in questions:
            Question.objects.create(
                exam_id=exam,
                question_type=q['type'],
                content=q['content'],
                options=q.get('options'),
                correct_answer=q['answer'],
                answer_type=q.get('answer_type', 'options')
            )
        return Response({"id": exam.exam_id,"message": "考试已发布"},status=200)


class TeacherGradeExamView(APIView):
    """教师批改考试"""

    def get(self, request, exam_id):
        """获取考试提交列表"""
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        submissions = ExamSubmission.objects.filter(
            exam_id=exam_id
        ).order_by('-submit_time')[(page - 1) * page_size: page * page_size]
        # ...原有处理逻辑
        submissions = ExamSubmission.objects.filter(exam_id=exam_id)
        result = []

        for sub in submissions:
            student_data = get_student(sub.student_id)
            result.append({
                "submission_id": sub.submission_id,
                "student_id": sub.student_id,
                "student_name": student_data.get("name", "未知") if student_data else "未知",
                "score": sub.score,
                "status": sub.status,
                "submit_time": sub.submit_time
            })

        return Response(result)

    def post(self, request, submission_id):
        """批改主观题"""
        submission = get_object_or_404(ExamSubmission, submission_id=submission_id)
        question_id = request.data.get("question_id")
        score = request.data.get("score")
        comment = request.data.get("comment", "")

        if not question_id or not score:
            return Response({"error": "缺少参数"}, status=400)

        # 更新主观题分数
        if "graded_answers" not in submission.meta:
            submission.meta["graded_answers"] = {}

        submission.meta["graded_answers"][question_id] = {
            "score": score,
            "comment": comment
        }

        # 重新计算总分
        total_score = submission.score or 0
        questions = Question.objects.filter(exam_id=submission.exam_id)

        for q in questions:
            if q.question_type in ['essay']:  # 主观题
                graded = submission.meta["graded_answers"].get(str(q.question_id), {})
                total_score += graded.get("score", 0)

        submission.score = total_score
        submission.status = "graded"
        submission.save()

        # 更新成绩表
        Grade.objects.update_or_create(
            student_id=submission.student_id,
            course_id=submission.exam.course_id,
            defaults={'grade': total_score}
        )

        return Response({"message": "批改成功"})


class StudentExamListView(APIView):
    """获取学生可参加的考试列表"""

    def get(self, request, student_id):
        # 获取学生已选课程
        enrolled_courses = Enrollment.objects.filter(
            student_id=student_id
        ).values_list('course_id', flat=True)

        # 获取这些课程的已发布考试
        now = timezone.now()
        exams = Exam.objects.filter(
            course_id__in=enrolled_courses,
            is_published=True
        ).annotate(
            can_start=Case(
                When(start_time__lte=now, end_time__gte=now, then=Value(True)),
                default=Value(False),
                output_field=BooleanField()
            )
        ).order_by('start_time')

        # 检查学生是否已经提交过
        exam_data = []
        for exam in exams:
            submission = ExamSubmission.objects.filter(
                exam_id=exam.exam_id,
                student_id=student_id
            ).first()

            exam_data.append({
                "exam_id": exam.exam_id,
                "exam_name": exam.exam_name,
                "exam_type": exam.exam_type,
                "course_id": exam.course_id.course_id,
                "course_name": exam.course_id.course_name,
                "start_time": exam.start_time,
                "end_time": exam.end_time,
                "time_limit": exam.time_limit,
                "can_start": exam.can_start,
                "has_submitted": submission is not None,
                "score": submission.score if submission else None,
                "status": submission.status if submission else None
            })

        return Response(exam_data)


class StudentExamDetailView(APIView):
    """获取考试详情并处理考试提交"""

    def get(self, request, exam_id, student_id):
        # 检查考试权限和状态
        exam = get_object_or_404(Exam, exam_id=exam_id)
        if not Enrollment.objects.filter(student_id=student_id, course_id=exam.course_id).exists():
            return Response({"error": "未选此课程"}, status=403)

        now = timezone.now()
        if not exam.is_published or now < exam.start_time or now > exam.end_time:
            return Response({"error": "考试不可用"}, status=403)

        # 获取题目
        questions = Question.objects.filter(exam_id=exam_id).order_by('question_id')
        question_serializer = QuestionSerializer(questions, many=True)

        # 获取或创建考试提交记录
        submission, created = ExamSubmission.objects.get_or_create(
            exam_id=exam_id,
            student_id=student_id,
            defaults={
                'start_time': now,
                'status': 'in_progress',
                'answers': {}
            }
        )

        return Response({
            "exam": ExamSerializer(exam).data,
            "questions": question_serializer.data,
            "submission": ExamSubmissionSerializer(submission).data,
            "remaining_time": (exam.end_time - now).total_seconds() if now < exam.end_time else 0
        })

    def post(self, request, exam_id, student_id):
        """提交考试答案"""
        exam = get_object_or_404(Exam, exam_id=exam_id)
        submission = get_object_or_404(ExamSubmission, exam_id=exam_id, student_id=student_id)

        if submission.status != 'in_progress':
            return Response({"error": "考试已提交"}, status=400)

        # 验证答案格式
        answers = request.data.get('answers', {})
        if not isinstance(answers, dict):
            return Response({"error": "答案格式错误"}, status=400)

        # 保存答案
        submission.answers = answers
        submission.status = 'submitted'
        submission.submit_time = timezone.now()
        submission.save()

        # 自动批改客观题
        self.auto_grade_submission(submission)

        return Response({"message": "提交成功"})

    def auto_grade_submission(self, submission):
        """自动批改客观题"""
        questions = Question.objects.filter(exam_id=submission.exam_id)
        total_score = 0

        for question in questions:
            if question.question_type in ['single_choice', 'true_false', 'fill_blank']:
                user_answer = submission.answers.get(str(question.question_id))
                correct_answer = question.correct_answer

                if user_answer == correct_answer:
                    total_score += question.score

        submission.score = total_score
        submission.save()

        # 更新成绩表
        Grade.objects.update_or_create(
            student_id=submission.student_id,
            course_id=submission.exam.course_id,
            defaults={'grade': total_score}
        )


class StudentExamCourseListView(APIView):
    """学生已选课程列表（含考试信息）"""

    def get(self, request, student_id):
        # 获取学生已选课程
        enrolled_courses = Enrollment.objects.filter(student_id=student_id)

        # 获取每个课程的考试信息
        course_data = []
        for enrollment in enrolled_courses:
            course = enrollment.course_id
            exams = Exam.objects.filter(
                course_id=course.course_id,
                is_published=True
            ).annotate(
                has_submitted=Case(
                    When(examsubmission__student_id=student_id, then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField()
                )
            )

            course_data.append({
                "course_id": course.course_id,
                "course_name": course.course_name,
                "course_cover": course.course_cover.url if course.course_cover else None,
                "exams": ExamSerializer(exams, many=True).data
            })

        return Response(course_data)


class TeacherExamCreateView(APIView):
    """教师创建考试"""

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            exam = serializer.save()
            return Response(ExamSerializer(exam).data, status=201)
        return Response(serializer.errors, status=400)


class TeacherQuestionCreateView(APIView):
    """教师添加考题"""

    def post(self, request, exam_id):
        exam = get_object_or_404(Exam, exam_id=exam_id)
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(exam_id=exam)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class StudentExamTakingView(APIView):
    """学生参加考试"""

    def get(self, request, exam_id, student_id):
        # # 检查IP变化
        # if request.META.get('HTTP_X_FORWARDED_FOR') != submission.meta.get('ip_address'):
        #     return Response({"error": "考试环境异常"}, status=403)
        #
        # # 检查浏览器指纹
        # browser_hash = generate_browser_hash(request)
        # if browser_hash != submission.meta.get('browser_hash'):
        #     return Response({"error": "考试环境异常"}, status=403)
        exam = get_object_or_404(Exam, exam_id=exam_id)

        # 检查学生是否选了这门课
        if not Enrollment.objects.filter(student_id=student_id, course_id=exam.course_id).exists():
            return Response({"error": "未选此课程"}, status=403)

        # 检查考试是否已发布且在有效期内
        now = timezone.now()
        if not exam.is_published or now < exam.start_time or now > exam.end_time:
            return Response({"error": "考试不可用"}, status=403)

        # 获取或创建考试提交记录
        submission, created = ExamSubmission.objects.get_or_create(
            exam_id=exam_id,
            student_id=student_id,
            defaults={
                'start_time': now,
                'status': 'in_progress',
                'answers': {}
            }
        )

        # 如果已经提交过，返回提交结果
        if submission.status != 'in_progress':
            return Response({
                "message": "已提交考试",
                "score": submission.score,
                "status": submission.status
            })

        # 获取考试题目
        questions = Question.objects.filter(exam_id=exam_id).order_by('question_id')

        return Response({
            "exam": ExamSerializer(exam).data,
            "questions": QuestionSerializer(questions, many=True).data,
            "remaining_time": (exam.end_time - now).total_seconds(),
            "submission_id": submission.submission_id
        })

    def post(self, request, exam_id, student_id):
        """提交考试答案"""
        exam = get_object_or_404(Exam, exam_id=exam_id)
        submission = get_object_or_404(ExamSubmission, exam_id=exam_id, student_id=student_id)

        if submission.status != 'in_progress':
            return Response({"error": "考试已提交"}, status=400)

        # 验证答案格式
        answers = request.data.get('answers', {})
        if not isinstance(answers, dict):
            return Response({"error": "答案格式错误"}, status=400)

        # 保存答案
        submission.answers = answers
        submission.status = 'submitted'
        submission.submit_time = timezone.now()
        submission.save()

        # 自动批改客观题
        self.auto_grade_submission(submission)

        return Response({"message": "提交成功"})

    def auto_grade_submission(self, submission):
        """自动批改客观题"""
        questions = Question.objects.filter(exam_id=submission.exam_id)
        total_score = 0

        for question in questions:
            if question.question_type in ['single_choice', 'true_false', 'fill_blank']:
                user_answer = submission.answers.get(str(question.question_id))
                correct_answer = question.correct_answer

                if user_answer == correct_answer:
                    total_score += question.score

        submission.score = total_score
        submission.save()

        # 更新成绩表
        Grade.objects.update_or_create(
            student_id=submission.student_id,
            course_id=submission.exam.course_id,
            defaults={'grade': total_score}
        )






