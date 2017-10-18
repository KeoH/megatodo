from rest_framework import serializers

from todos.models import Todo

from ..mixins.serializers import StatusSerializerMixin
from .task import TaskSerializer
from .user import UserSimpleSerializer
from .comment import CommentSerializer

class TodoSerializer(StatusSerializerMixin):

    tasks = TaskSerializer(many=True)
    comments_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    author = UserSimpleSerializer()

    class Meta:
        model = Todo
        fields = (
            'id', 'title', 'author', 'status', 'status_verbose', 
            'is_complete', 'is_canceled', 'is_expired', 'due_date', 
            'comments_count', 'comments', 'body', 'tasks', 'create_date', 
            'update_date'
        )

    def get_comments_count(self, obj):
        return obj.comments.count()