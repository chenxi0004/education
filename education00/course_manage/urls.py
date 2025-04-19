
# course_management/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CourseViewSet,  GradeViewSet, CourseDetailView, VerifyTokenView, StudentEnrollmentView,
                    LearningProgressView, LearningRecordView, LearningReportView,CourseSearchView,StudentUnenrollmentView,
                    StudentEnrollmentListView,EnrolledCoursesView,StudentCourseVideosView,ChapterViewSet,
                    ExamViewSet,ExamSubmissionViewSet,QuestionViewSet,TeacherGradeExamView,TeacherExamPublishView,
                    TeacherExamManagementView,TeacherQuestionManagementView,StudentExamListView,StudentExamDetailView,
                    StudentExamCourseListView, TeacherExamCreateView,
                    TeacherQuestionCreateView, StudentExamTakingView
                    )

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'exams', ExamViewSet)
router.register('questions', QuestionViewSet)
router.register('exam-submissions', ExamSubmissionViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('courses/<str:course_id>/', CourseDetailView.as_view(), name='course-detail'),
    path('verify/', VerifyTokenView.as_view(), name='verify-token'),
    path('enroll/<str:course_id>/', StudentEnrollmentView.as_view(), name='student-enroll'),
    path('progress/<str:course_id>/', LearningProgressView.as_view(), name='learning-progress'),
    path('record/<str:course_id>/', LearningRecordView.as_view(), name='learning-record'),
    path('report/', LearningReportView.as_view(), name='learning-report'),
    path('courses/search/', CourseSearchView.as_view(), name='course-search'),
    path('unenroll/<str:course_id>/', StudentUnenrollmentView.as_view(), name='student-unenroll'),
    path('enroll/list/', StudentEnrollmentListView.as_view(), name='student-enroll-list'),
    path('enrollments/', EnrolledCoursesView.as_view(), name='enrolled-courses'),
    path('student/<str:student_id>/course/<str:course_id>/videos/', StudentCourseVideosView.as_view(), name='student-course-videos'),
    path('chapters/', ChapterViewSet.as_view({'get': 'list', 'post': 'create'}), name='chapter-list'),
    path('chapters/<int:pk>/', ChapterViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='chapter-detail'),
    path('courses/<str:course_id>/chapters/', ChapterViewSet.as_view({'get': 'list'}), name='course-chapters'),
    # 记录学习时长
    path('learning-records/', LearningRecordView.as_view(), name='learning-record'),
    # 更新学习进度
    path('learning-progress/<str:student_id>/<str:course_id>/', LearningProgressView.as_view(), name='learning-progress'),
    # 获取学习报告
    path('learning-report/<str:student_id>/', LearningReportView.as_view(), name='learning-report'),



    path('student/exams/<str:course_id>/', StudentExamListView.as_view(), name='student-exams'),
    path('student/exam-record/<int:exam_id>/', StudentExamDetailView.as_view(), name='student-exam-record'),
    path('student/<str:student_id>/courses/', StudentExamCourseListView.as_view(), name='student-exam-courses'),
    path('teacher/exam/create/', TeacherExamCreateView.as_view(), name='teacher-exam-create'),
    path('teacher/exam/publish/', TeacherExamPublishView.as_view(), name='teacher-exam-publish'),
    path('teacher/exam/grade/',TeacherGradeExamView.as_view(), name='teacher-exam-grade'),
    path('teacher/exam/<int:exam_id>/questions/', TeacherQuestionCreateView.as_view(), name='teacher-question-create'),
    path('student/<str:student_id>/exam/<int:exam_id>/', StudentExamTakingView.as_view(), name='student-exam-taking'),


]