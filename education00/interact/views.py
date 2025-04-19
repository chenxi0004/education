from datetime import timezone

from django.db import transaction
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment,Notification
from .serializers import CommentSerializer,NotificationSerializer


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get_queryset(self):
    #     course_id = self.request.GET.get('course_id')
    #     if course_id:
    #         # 获取课程的所有顶级评论（没有父评论的评论）
    #         return Comment.objects.filter(course_id=course_id, parent=None)
    #     return super().get_queryset()

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        topic = self.request.GET.get('topic')
        if course_id and topic:
            # 获取课程的所有顶级评论（没有父评论的评论），并按话题过滤
            return Comment.objects.filter(course_id=course_id, parent=None, topic=topic)
        elif course_id:
            # 获取课程的所有顶级评论（没有父评论的评论）
            return Comment.objects.filter(course_id=course_id, parent=None)
        return super().get_queryset()

    @action(detail=False, methods=['get'])
    def by_topic(self, request):
        course_id = request.GET.get('course_id')
        if not course_id:
            return Response({'error': 'course_id is required'}, status=400)

        # 获取课程的所有话题
        topics = Comment.objects.filter(course_id=course_id).values_list('topic', flat=True).distinct()
        topic_comments = []

        for topic in topics:
            comments = Comment.objects.filter(course_id=course_id, topic=topic, parent=None)
            topic_comments.append({
                'topic': topic,
                'comments': CommentSerializer(comments, many=True).data
            })

        return Response(topic_comments)


from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        student_id = self.request.GET.get('student_id')
        if student_id:
            return Notification.objects.filter(student_id=student_id)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class SendNotificationView(APIView):
#
#     def post(self, request):
#         student_id = request.data.get('student_id')
#         message = request.data.get('message')
#
#         if not student_id or not message:
#             return Response({'error': 'Student ID and message are required'}, status=400)
#
#         Notification.objects.create(student_id=student_id, message=message)
#         return Response({'message': 'Notification sent successfully'})


class SendNotificationView(APIView):
    def post(self, request):
        # 获取学生ID列表和消息内容
        student_ids = request.data.get('student_ids')
        student_id = request.data.get('student_id')
        message = request.data.get('message')

        # 基础参数校验
        if not student_ids or not message:
            if not student_id:
                return Response({'error': 'student_id is required'}, status=400)
            else:
                Notification.objects.create(student_id=student_id, message=message)
                return Response({'message': 'Notification sent successfully'})

        # 验证student_ids是否为列表类型
        if not isinstance(student_ids, list):
            return Response({'error': 'Student IDs must be a list'}, status=400)

        # 使用批量创建提高效率（比循环create快10倍以上）
        try:
            with transaction.atomic():
                notifications = [
                    Notification(student_id=sid, message=message)
                    for sid in student_ids
                ]
                Notification.objects.bulk_create(notifications)
        except Exception as e:
            # 处理无效学生ID的情况
            return Response({'error': 'Invalid student ID(s) detected'}, status=400)

        return Response({'message': f'Sent {len(student_ids)} notifications successfully'})


# class SendNotificationView(APIView):
#     def post(self, request):
#         # 统一接收参数
#         data = request.data
#         student_id = data.get('student_id')
#         student_ids = data.get('student_ids')
#         message = data.get('message')
#
#         # 参数校验
#         if not message:
#             return Response({'error': '消息内容不能为空'}, status=400)
#
#         # 单个发送逻辑
#         if student_id and not student_ids:
#             try:
#                 Notification.objects.create(
#                     student_id=student_id,
#                     message=message,
#                     created_at=timezone.now()
#                 )
#                 return Response({'message': '通知发送成功'})
#             except Exception:
#                 return Response({'error': '无效的接收人ID'}, status=400)
#
#         # 批量发送逻辑
#         elif student_ids and not student_id:
#             if not isinstance(student_ids, list):
#                 return Response({'error': '学生ID必须为列表格式'}, status=400)
#
#             try:
#                 with transaction.atomic():
#                     Notification.objects.bulk_create([
#                         Notification(student_id=sid, message=message)
#                         for sid in student_ids
#                     ])
#                 return Response({'message': f'成功发送 {len(student_ids)} 条通知'})
#             except Exception as e:
#                 return Response({'error': '检测到无效的学生ID'}, status=400)
#
#         # 参数冲突校验
#         else:
#             return Response({'error': '不能同时提供单个ID和批量ID'}, status=400)