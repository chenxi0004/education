from rest_framework import permissions

class IsTeacher(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     return request.user.is_authenticated and hasattr(request.user, "teacher_id")
    pass

class IsStudent(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     return request.user.is_authenticated and hasattr(request.user, "student_id")
    pass