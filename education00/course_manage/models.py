# -*- coding: utf-8 -*-
# Create your models here.
#course_material/models.py

from django.db import models
from django.utils import timezone
from .utils import get_student, get_teacher

# 课程表
class Course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True, verbose_name="课程编号")
    course_name = models.CharField(max_length=100, verbose_name="课程名称")
    course_cover = models.ImageField(upload_to="course_covers/", null=True, verbose_name="课程封面")
    course_intro = models.TextField(verbose_name="课程简介")
    course_type = models.CharField(max_length=50, verbose_name="课程类型")
    teacher_id = models.CharField(max_length=20, verbose_name="授课教师编号")
    start_time = models.DateTimeField(verbose_name="开课时间")
    end_time = models.DateTimeField(verbose_name="结课时间")
    total_video_duration = models.FloatField(default=0.0, verbose_name="课程视频总时长（分钟）",blank=True, null=True)

    @property
    def get_teacher_name(self):
        try:
            teacher_data = get_teacher(self.teacher_id)
            return teacher_data["teacher_name"]
        except Exception as e:
            return "Unknown Teacher"

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = "course"
        # extra_kwargs = {
        #     "course_cover": {"required": False, "allow_null": True},  # 允许为空
        #     "course_intro": {"required": True},
        #     "course_type": {"required": True}
        # }

class Chapter(models.Model):
    chapter_id = models.AutoField(primary_key=True, verbose_name="章节编号")
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="课程编号")
    chapter_name = models.CharField(max_length=100, verbose_name="章节名称")
    chapter_order = models.IntegerField(verbose_name="章节顺序")

    class Meta:
        db_table = "chapter"
        ordering = ['chapter_order']  # 按章节顺序排序

    def __str__(self):
        return f"{self.course_id.course_name} - {self.chapter_name}"


# 选课表
class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True, verbose_name="选课编号")
    teacher_id = models.CharField(max_length=20, verbose_name="授课教师编号")
    student_id = models.CharField(max_length=20, verbose_name="学生编号")
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="课程编号")
    enrollment_time = models.DateTimeField(default=timezone.now, verbose_name="选课时间")

    @property
    def teacher_name(self):
        try:
            teacher_data = get_teacher(self.teacher_id)
            return teacher_data["teacher_name"]
        except Exception as e:
            return "Unknown Teacher"

    @property
    def get_student_name(self):
        try:
            student_data = get_student(self.student_id)
            return student_data["student_name"]
        except Exception as e:
            return "Unknown Student"

    class Meta:
        db_table = "enrollment"
        unique_together = ("student_id", "course_id")  # 一个学生不能重复选同一门课程


# 成绩表
class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True, verbose_name="成绩编号")
    student_id = models.CharField(max_length=20, verbose_name="学生编号")
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="课程编号")
    grade = models.FloatField(verbose_name="成绩")

    @property
    def get_course_name(self):
        return self.course_id.course_name
    @property
    def get_student_name(self):
        try:
            student_data = get_student(self.student_id)
            return student_data["student_name"]
        except Exception as e:
            return "Unknown Student"

    class Meta:
       db_table = "grade"
       # unique_together = ("student_id", "course_id")  # 一个学生对一门课程只有一个成绩


class LearningProgress(models.Model):
    student_id = models.CharField(max_length=20, verbose_name="学生编号")
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="课程编号")
    progress = models.FloatField(default=0.0, verbose_name="学习进度（百分比）")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")

    class Meta:
        db_table = "learning_progress"
        unique_together = ("student_id", "course_id")


class LearningRecord(models.Model):
    record_id = models.AutoField(primary_key=True, verbose_name="记录编号")
    student_id = models.CharField(max_length=20, verbose_name="学生编号")
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="课程编号")
    material_id = models.ForeignKey('course_material.Material', on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name="学习资料编号")
    video_id = models.ForeignKey('course_material.Video', on_delete=models.CASCADE, null=True, blank=True, verbose_name="学习视频编号")
    content = models.TextField(verbose_name="学习内容")
    duration = models.FloatField(verbose_name="学习时长（分钟）")
    record_time = models.DateTimeField(default=timezone.now, verbose_name="记录时间")
    is_completed = models.BooleanField(default=False, verbose_name="是否完播")  # 添加 is_completed 字段

    class Meta:
        db_table = "learning_record"




from django.db import models
from django.utils import timezone


class Exam(models.Model):
    EXAM_TYPES = [
        ('midterm', '期中考试'),
        ('final', '期末考试'),
        ('quiz', '小测验'),
        ('custom', '自定义考试'),
    ]

    exam_id = models.AutoField(primary_key=True, verbose_name="考试编号")
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="所属课程")
    exam_name = models.CharField(max_length=100, verbose_name="考试名称")
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPES,default='custom', verbose_name="考试类型")
    description = models.TextField(verbose_name="考试说明", blank=True)
    total_score = models.IntegerField(verbose_name="总分", default=100)
    time_limit = models.IntegerField(verbose_name="考试时长(分钟)", default=60)
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    is_published = models.BooleanField(default=False, verbose_name="是否发布")
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "exam"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.course_id.course_name} - {self.exam_name}"

    @property
    def status(self):
        now = timezone.now()
        if now < self.start_time:
            return "未开始"
        elif now > self.end_time:
            return "已结束"
        else:
            return "进行中"


class Question(models.Model):
    QUESTION_TYPES = [
        ('single_choice', '单选题'),
        ('multiple_choice', '多选题'),
        ('true_false', '判断题'),
        ('fill_blank', '填空题'),
        ('essay', '问答题'),
    ]

    question_id = models.AutoField(primary_key=True, verbose_name="题目编号")
    exam_id = models.ForeignKey('Exam', on_delete=models.CASCADE, verbose_name="所属考试")
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES,default='single_choice', verbose_name="题目类型")
    content = models.TextField(verbose_name="题目内容")
    options = models.JSONField(verbose_name="选项", blank=True, null=True)  # 用于选择题的选项
    correct_answer = models.JSONField(verbose_name="正确答案",default=dict)  # 存储JSON或文本
    score = models.IntegerField(verbose_name="分值", default=1)
    difficulty = models.IntegerField(verbose_name="难度系数", default=1,
                                     choices=[(1, '简单'), (2, '中等'), (3, '困难')])
    # 在Question模型中增加题目解析字段
    analysis = models.TextField(verbose_name="题目解析", blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    class Meta:
        db_table = "question"
        ordering = ['question_id']

    def __str__(self):
        return f"{self.get_question_type_display()} - {self.content[:50]}"


class ExamSubmission(models.Model):
    SUBMISSION_STATUS = [
        ('in_progress', '考试中'),
        ('submitted', '已提交'),
        ('graded', '已批改'),
    ]

    submission_id = models.AutoField(primary_key=True, verbose_name="提交编号")
    exam_id = models.ForeignKey('Exam', on_delete=models.CASCADE, verbose_name="所属考试")
    student_id = models.CharField(max_length=20, verbose_name="学生编号")
    answers = models.JSONField(verbose_name="学生答案", default=dict)  # 存储学生答案
    score = models.FloatField(verbose_name="得分", null=True, blank=True)
    start_time = models.DateTimeField(verbose_name="开始时间")
    submit_time = models.DateTimeField(verbose_name="提交时间", null=True, blank=True)
    status = models.CharField(max_length=20, choices=SUBMISSION_STATUS, default='in_progress', verbose_name="状态")
    teacher_comment = models.TextField(verbose_name="教师评语", blank=True)

    class Meta:
        db_table = "exam_submission"
        unique_together = ('exam_id', 'student_id')  # 一个学生只能提交一次考试

    def __str__(self):
        return f"{self.exam_id.exam_name} - {self.student_id}"

    @property
    def time_spent(self):
        if self.submit_time:
            return (self.submit_time - self.start_time).total_seconds() / 60
        return None

    @property
    def time_remaining(self):
        if self.status == 'in_progress':
            exam = self.exam_id
            total_time = exam.time_limit * 60  # 转换为秒
            time_elapsed = (timezone.now() - self.start_time).total_seconds()
            return max(0, total_time - time_elapsed)
        return 0