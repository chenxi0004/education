from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Material,Video
from course_manage.models import Enrollment, LearningProgress, LearningRecord
from .serializers import MaterialSerializer,VideoSerializer
# Create your views here.
import time

def generate_course_related_filename(course_id, filename):
    ext = filename.split('.')[-1]
    timestamp = int(time.time())
    unique_name = f"{course_id}_{timestamp}.{ext}"
    return unique_name
class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]  # 学生可以查看
        return [permissions.AllowAny()]  # 教师可以上传

    def create(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        if not course_id:
            return Response({"error": "Course ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        # 检查当前用户是否是课程的创建者
        if course.teacher_id != request.data.get('student_or_teacher_id'):
            return Response({"error": "You do not have permission to upload materials for this course"},
                            status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]  # 学生可以查看
        return [permissions.AllowAny()]  # 教师可以上传


    def get_queryset(self):
        chapter_id = self.request.data.get('chapter_id')
        if chapter_id:
            return Video.objects.filter(chapter_id=chapter_id)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from .models import Material
from course_manage.models import Course



class UploadVideoView(APIView):
    def post(self, request, course_id):
        if not course_id:
            course_id = request.data.get('course_id')
            if not course_id:
                return Response({"error": "Course ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        teacher_id = request.data.get('student_or_teacher_id')
        # if not teacher_id:
        #     return Response({"error": "Teacher ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        print(course.teacher_id,teacher_id)
        # # 检查当前用户是否是课程的创建者
        #     if course.teacher_id != teacher_id:
        #         return Response({"error": "You do not have permission to upload videos for this course"},
        #                         status=status.HTTP_403_FORBIDDEN)

        video_file = request.FILES.get('video_file')
        if not video_file:
            return Response({"error": "No video file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # fs = FileSystemStorage(location="course_video/")
        # unique_filename = generate_course_related_filename(course_id, video_file.name)
        # filename = fs.save(unique_filename, video_file)
        fs = FileSystemStorage()  # 使用默认存储
        unique_filename = generate_course_related_filename(course_id, video_file.name)
        filename = fs.save(f"course_video/{unique_filename}", video_file)
        file_url = fs.url(filename)  # 生成的 URL 是 /media/course_video/...
        print('路径',file_url)



        video = Video.objects.create(
            course_id=course,
            video_name=video_file.name,
            video_file=filename,
            review_status='pending'  # 设置审核状态为待审核
        )

        # 更新所有已选该课程的学生的学习进度
        self.update_students_learning_progress(course_id, video.video_duration)

        return Response({"message": "Video uploaded successfully", "video_id": video.video_id},
                        status=status.HTTP_201_CREATED)

    def update_students_learning_progress(self, course_id, video_duration):
        """
        更新所有已选该课程的学生的学习进度
        """
        course = Course.objects.get(course_id=course_id)
        students = Enrollment.objects.filter(course_id=course).values_list('student_id', flat=True)

        for student_id in students:
            try:
                progress, created = LearningProgress.objects.get_or_create(student_id=student_id, course_id=course_id)
                completed_videos = LearningRecord.objects.filter(student_id=student_id, course_id=course_id,
                                                                 is_completed=True)
                total_completed_duration = sum(record.video_id.video_duration for record in completed_videos)
                progress.progress = (total_completed_duration / course.total_video_duration) * 100
                progress.progress = min(progress.progress, 100)  # 限制进度不超过 100%
                progress.save()
            except Exception as e:
                print(f"Error updating progress for student {student_id}: {e}")

    
    
# 视频审核接口
class MaterialReviewView(APIView):
    # permission_classes = [IsAuthenticated]  # 确保只有管理员可以审核

    def post(self, request, material_id):
        try:
            material = Material.objects.get(material_id=material_id)#通过url获取material_id
        except Material.DoesNotExist:
            return Response({"error": "Material not found"},status=status.HTTP_404_NOT_FOUND)

        review_status = request.data.get('review_status')
        if review_status not in ['approved', 'rejected','re-review']:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

        # 如果状态是 're-review'，则将视频状态重置为 'pending'
        if review_status == 're-review':
            material.review_status = 'pending'
            material.save()
            return Response({"message": "Video re-review initiated", "status": material.review_status},
                            status=status.HTTP_200_OK)

        material.review_status = review_status
        material.save()
        # 返回最新的审核状态
        return Response({"message": "Material reviewed successfully", "status": material.review_status},
                        status=status.HTTP_200_OK)


class VideoReviewView(APIView):
    # permission_classes = [IsAuthenticated]  # 确保只有管理员可以审核

    def post(self, request, video_id):
        try:
            video = Video.objects.get(video_id=video_id)#通过url获取material_id
        except Video.DoesNotExist:
            return Response({"error": "Material not found"},status=status.HTTP_404_NOT_FOUND)

        review_status = request.data.get('review_status')
        if review_status not in ['approved', 'rejected','re-review']:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
        # 如果状态是 're-review'，则将视频状态重置为 'pending'
        if review_status == 're-review':
            video.review_status = 'pending'
            video.save()
            return Response({"message": "Video re-review initiated", "status": video.review_status},
                            status=status.HTTP_200_OK)
        video.review_status = review_status
        video.save()
        # 返回最新的审核状态
        return Response({"message": "Material reviewed successfully", "status": video.review_status},
                        status=status.HTTP_200_OK)