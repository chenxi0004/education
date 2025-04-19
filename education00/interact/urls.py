from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet,NotificationViewSet,SendNotificationView

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send-notification/', SendNotificationView.as_view(), name='send-notification'),
]