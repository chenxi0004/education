from django.apps import AppConfig


class CourseManageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course_manage'

    def ready(self):
        import course_manage.signals
