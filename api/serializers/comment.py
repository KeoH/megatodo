from rest_framework import serializers

from todos.models import Comment
from .user import UserSimpleSerializer

class CommentSerializer(serializers.ModelSerializer):

    author = UserSimpleSerializer()

    class Meta:
        model = Comment
        fields = ('id','author', 'message', 'create_date', 'update_date')