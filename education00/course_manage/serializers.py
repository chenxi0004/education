from rest_framework import serializers
from .models import Course, Enrollment, Grade, LearningProgress, LearningRecord,Chapter
from .utils import get_student, get_teacher


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = "__all__"
class CourseSerializer(serializers.ModelSerializer):
    enrolled = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_enrolled(self, obj):
        return getattr(obj, 'enrolled', False)

class ChapterSerializer(serializers.ModelSerializer):
    enrolled = serializers.SerializerMethodField()
    class Meta:
        model = Chapter
        fields = '__all__'
        extra_kwargs = {
            'chapters': {'default': []},  # 默认值为空列表
        }

    def get_enrolled(self, obj):
        # 通过 Chapter 的 course_id 获取关联的 Course 对象
        course = obj.course_id
        # 返回 Course 的 enrolled 属性
        return getattr(course, 'enrolled', True)

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"

class LearningProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningProgress
        fields = "__all__"


class LearningRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningRecord
        fields = "__all__"


from rest_framework import serializers
from rest_framework import serializers
from .models import Exam, Question, ExamSubmission

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ExamSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSubmission
        fields = '__all__'

#
# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = '__all__'
#         extra_kwargs = {
#             'correct_answer': {'write_only': True}  # 正确答案不返回给学生
#         }
#
#
# class ExamSerializer(serializers.ModelSerializer):
#     questions = QuestionSerializer(many=True, read_only=True)
#     status = serializers.CharField(source='get_status_display', read_only=True)
#
#     class Meta:
#         model = Exam
#         fields = '__all__'
#         read_only_fields = ('created_at', 'updated_at')
#
#
# class ExamDetailSerializer(serializers.ModelSerializer):
#     questions = QuestionSerializer(many=True, read_only=True)
#     course_name = serializers.CharField(source='course_id.course_name', read_only=True)
#     course_cover = serializers.SerializerMethodField()
#     teacher_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Exam
#         fields = ['exam_id', 'exam_name', 'exam_type', 'course_id', 'course_name',
#                   'course_cover', 'description', 'total_score', 'time_limit',
#                   'start_time', 'end_time', 'status', 'questions', 'teacher_name']
#
#     def get_course_cover(self, obj):
#         if obj.course_id.course_cover:
#             return self.context['request'].build_absolute_uri(obj.course_id.course_cover.url)
#         return None
#
#     def get_teacher_name(self, obj):
#         teacher_data = get_teacher(obj.course_id.teacher_id)
#         return teacher_data.get('teacher_name', 'Unknown') if teacher_data else 'Unknown'
# class ExamListSerializer(serializers.ModelSerializer):
#     course_name = serializers.CharField(source='course_id.course_name', read_only=True)
#     course_cover = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Exam
#         fields = ('exam_id', 'exam_name', 'exam_type', 'course_id', 'course_name',
#                   'course_cover', 'start_time', 'end_time', 'status', 'is_published')
#
#     def get_course_cover(self, obj):
#         if obj.course_id.course_cover:
#             return self.context['request'].build_absolute_uri(obj.course_id.course_cover.url)
#         return None
#
#
# class ExamSubmissionSerializer(serializers.ModelSerializer):
#     student_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = ExamSubmission
#         fields = '__all__'
#         read_only_fields = ('submission_id', 'score', 'status', 'teacher_comment')
#
#     def get_student_name(self, obj):
#         student_data = get_student(obj.student_id)
#         return student_data.get('student_name', 'Unknown') if student_data else 'Unknown'
#
#
# class StudentAnswerSerializer(serializers.Serializer):
#     question_id = serializers.IntegerField()
#     answer = serializers.CharField()
