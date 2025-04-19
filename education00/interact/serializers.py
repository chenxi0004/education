from rest_framework import serializers
from .models import Comment,Notification

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('created_time',)  # 设置为只读字段

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveField(many=True, read_only=True)
    reply_to = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        # fields = ['comment_id', 'course_id', 'user_id', 'user_role', 'content', 'created_time', 'parent', 'replies']
        fields = ['comment_id', 'course_id', 'user_id', 'user_role', 'content', 'created_time', 'parent', 'topic',
                  'replies', 'reply_to']
        read_only_fields = ('created_time',)

    def get_reply_to(self, obj):
        if obj.parent:
            return obj.parent.user_id  # 返回被回复者的用户ID
        return None

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'