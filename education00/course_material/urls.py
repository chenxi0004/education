from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import MaterialViewSet,  UploadVideoView,MaterialReviewView,VideoViewSet,VideoReviewView

router = DefaultRouter()
router.register(r'materials', MaterialViewSet)
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-video/<str:course_id>/', UploadVideoView.as_view(), name='upload-video'),
    path('review/<int:material_id>/', MaterialReviewView.as_view(), name='material-review'),
    path('videoreview/<int:video_id>/', VideoReviewView.as_view(), name='video-review'),

]