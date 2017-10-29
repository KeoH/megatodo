'''
    Module for ToDo serializer
'''

from rest_framework import serializers

from todos.models import Todo

from ..mixins.serializers import StatusSerializerMixin
from .task import TaskSerializer
from .user import UserSimpleSerializer
from .comment import CommentSerializer

class TodoSerializer(StatusSerializerMixin):
    '''
        Basic serializer of the ToDo model
    '''

    tasks = TaskSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    author = UserSimpleSerializer(read_only=True)

    class Meta:
        '''
            The meta class
        '''
        model = Todo
        fields = (
            'id', 'title', 'author', 'status', 'status_verbose', 
            'is_complete', 'is_canceled', 'is_expired', 'due_date', 
            'comments_count', 'comments', 'body', 'tasks', 'create_date', 
            'update_date',)

    def get_comments_count(self, obj):
        '''
            Counts elements for serializer
        '''
        return obj.comments.count()
