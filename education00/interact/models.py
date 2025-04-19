from django.db import models

# Create your models here.
from django.db import models

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, verbose_name="评论编号")
    course_id = models.ForeignKey('course_manage.Course', on_delete=models.CASCADE, verbose_name="课程编号")
    user_id = models.CharField(max_length=20, verbose_name="用户编号")
    user_role = models.CharField(max_length=100, verbose_name="用户角色")  # 'student' 或 'teacher'
    content = models.TextField(verbose_name="评论内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name="父评论")
    topic = models.CharField(max_length=100, verbose_name="话题", default="默认话题")  # 添加话题字段
    reply_to = models.CharField(max_length=50, null=True, blank=True, verbose_name="被回复者用户ID")  # 添加被回复者字段

    def __str__(self):
        return f"Comment by {self.user_id} on {self.course_id.course_name}"

    class Meta:
        db_table = "comment"


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True, verbose_name="通知编号")
    student_id = models.CharField(max_length=20, verbose_name="学生编号")
    message = models.TextField(verbose_name="通知内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    is_read = models.BooleanField(default=False, verbose_name="是否已读")

    class Meta:
        db_table = "notification"
        ordering = ['-created_at']

    def __str__(self):
        return f"通知 {self.notification_id} - {self.student_id}"