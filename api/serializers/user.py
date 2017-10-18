from django.contrib.auth.models import User, Group

from rest_framework import serializers

from ..mixins.serializers import AvatarSerializerMixin

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(AvatarSerializerMixin):

    
    groups = GroupSerializer(many=True)
    groups_list = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'groups', 'groups_list')

    def get_groups_list(self, obj):
        return [group.name for group in obj.groups.all() ]

class UserSimpleSerializer(AvatarSerializerMixin):

    class Meta:
        model = User
        fields = ('username', 'avatar')