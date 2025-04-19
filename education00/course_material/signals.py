from django.db.models.signals import post_save
from django.dispatch import receiver
from course_material.models import Video
from course_manage.models import Course
from django.db.models import Sum

@receiver(post_save, sender=Video)
def update_course_total_duration(sender, instance, **kwargs):
    # 获取课程对象
    course = instance.course_id

    # 计算课程中所有视频的总时长
    total_duration = Video.objects.filter(course_id=course).aggregate(total_duration=Sum('video_duration'))['total_duration'] or 0

    # 更新课程的总视频时长
    course.total_video_duration = total_duration
    course.save()