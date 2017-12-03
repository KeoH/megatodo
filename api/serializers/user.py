'''
    Module for user related serializers
'''

from django.contrib.auth.models import User, Group

from rest_framework import serializers

from ..mixins.serializers import AvatarSerializerMixin

class GroupSerializer(serializers.ModelSerializer):
    '''
        Group serializer
    '''
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(AvatarSerializerMixin):
    '''
        User serializer
    '''
    
    groups = GroupSerializer(many=True)
    groups_list = serializers.SerializerMethodField()

    class Meta:
        model = User
        lookup_field = 'username'
        fields = ('pk','username', 'email', 'avatar', 'groups', 'groups_list')

    def get_groups_list(self, obj):
        return [group.name for group in obj.groups.all() ]


class UserSimpleSerializer(AvatarSerializerMixin):
    '''
        Simplified version of the user serializer
    '''
    class Meta:
        model = User
        lookup_field = 'username'
        fields = ('username', 'avatar', 'pk')