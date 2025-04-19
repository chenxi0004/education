# from django.urls import path
# from teacher_or_student.views import StudentViewSet, TeacherViewSet
#
# urlpatterns = [
#     path("student", StudentViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'}),
#          name="student"),
#     path("teacher", TeacherViewSet.as_view({"get": "list", 'post': 'create', 'delete': 'destroy', 'put': 'update'}),
#          name='teacher'), ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import StudentViewSet, TeacherViewSet
#
# router = DefaultRouter()
# router.register(r'students', StudentViewSet, basename='student')
# router.register(r'teachers', TeacherViewSet, basename='teacher')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path
from teacher_or_student.views import ListAllStudents, ActionView, SearchView, SaveView, CheckView, TeacherList, \
    TeacherDetail

# router = DefaultRouter()
# router.register(r'teachers', TeacherViewSet, basename='teacher')
urlpatterns = [
    path('list', ListAllStudents.as_view(), name='list'),
    path('search', SearchView.as_view(), name='search'),
    path('save', SaveView.as_view(), name='save'),
    path('check', CheckView.as_view(), name='check'),
    path('action', ActionView.as_view(), name='action'),
    path('teachers/', TeacherList.as_view(), name='teacher-list'),  # 获取教师列表和创建教师
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),  # 获取、更新和删除单个教师
    # path('', include(router.urls)),
]
