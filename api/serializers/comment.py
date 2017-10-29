'''
    Serializer for Comment model
'''

from rest_framework import serializers

from todos.models import Comment
from .user import UserSimpleSerializer

class CommentSerializer(serializers.ModelSerializer):
    '''
        Serializer for Comment model
    '''
    
    author = UserSimpleSerializer()

    class Meta:
        model = Comment
        fields = ('id','author', 'message', 'create_date', 'update_date',)
