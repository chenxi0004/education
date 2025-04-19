from rest_framework import serializers
from .models import Material,Video


class MaterialSerializer(serializers.ModelSerializer):
    material_file_url = serializers.SerializerMethodField()
    course_id_display = serializers.SerializerMethodField()

    class Meta:
        model = Material
        fields = '__all__'  # 或者显式列出需要的字段

    def get_material_file_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.material_file.url)

    def get_course_id_display(self, obj):
        return obj.course_id.course_id


class VideoSerializer(serializers.ModelSerializer):
    video_file_url = serializers.SerializerMethodField()
    course_id_display = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__'  # 或者显式列出需要的字段

    def get_video_file_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.video_file.url)

    def get_course_id_display(self, obj):
        return obj.course_id.course_id
