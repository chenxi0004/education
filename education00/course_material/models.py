from django.db import models
from moviepy.video.io.VideoFileClip import VideoFileClip


# from course_manage.models import Course
# Create your models here.



# 课程资料表
class Material(models.Model):
    material_id = models.AutoField(primary_key=True, verbose_name="资料编号")
    course_id = models.ForeignKey('course_manage.Course', on_delete=models.CASCADE, verbose_name="课程编号")
    material_name = models.CharField(max_length=200, verbose_name="资料名称")
    material_file = models.FileField(upload_to="course_materials/", verbose_name="课程资料")
    MATERIAL_TYPES = (
        ('doc', 'Word 文档'),
        ('pdf', 'PDF 文档'),
        ('ppt', 'PPT 幻灯片'),
        ('mp4', '视频文件'),
        ('jpg', '图片文件'),
        ('other', '其他'),
    )
    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPES, blank=True)
    STATUS_CHOICES = (
        ('pending', '待审核'),
        ('approved', '审核通过'),
        ('rejected', '审核不通过'),
    )
    review_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="审核状态")

    # 添加一个方法来获取文件的完整 URL
    @property
    def material_file_url(self):
        try:
            return self.material_file.url
        except ValueError:
            return ""

    class Meta:
        db_table = "material"



class Video(models.Model):
    video_id = models.AutoField(primary_key=True, verbose_name="资料编号")
    course_id = models.ForeignKey('course_manage.Course', on_delete=models.CASCADE, verbose_name="课程编号")
    video_name = models.CharField(max_length=200, verbose_name="资料名称")
    video_file = models.FileField(upload_to="course_video/", verbose_name="课程视频")
    video_duration = models.FloatField(verbose_name="视频时长（分钟）",blank=True,null=True)
    STATUS_CHOICES = (
        ('pending', '待审核'),
        ('approved', '审核通过'),
        ('rejected', '审核不通过'),
    )
    review_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="审核状态")
    chapter_id = models.ForeignKey('course_manage.Chapter', on_delete=models.CASCADE, verbose_name="章节编号", null=True, blank=True)

    # 添加一个方法来获取文件的完整 URL
    @property
    def video_file_url(self):
        try:
            return self.video_file.url
        except ValueError:
            return ""

    def save(self, *args, **kwargs):
        # 如果是新上传的视频文件，计算视频时长
        if self.video_file and not self.video_duration:
            video_path = self.video_file.path
            with VideoFileClip(video_path) as video:
                # 获取视频时长（单位：秒），转换为分钟
                self.video_duration = video.duration / 60

        # 调用父类的 save 方法保存视频
        super().save(*args, **kwargs)

        # 更新课程的总视频时长
        self.update_course_total_duration()

    def update_course_total_duration(self):
        # 获取课程中所有视频的总时长
        total_duration = \
        Video.objects.filter(course_id=self.course_id).aggregate(total_duration=models.Sum('video_duration'))[
            'total_duration'] or 0

        # 更新课程的总视频时长
        self.course_id.total_video_duration = total_duration
        self.course_id.save()

    class Meta:
        db_table = "video"