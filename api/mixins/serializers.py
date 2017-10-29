'''
    Mixins for serializers
'''

from rest_framework import serializers

class StatusSerializerMixin(serializers.ModelSerializer):
    '''
        Mixin for the serialize status verbose
    '''
    status_verbose = serializers.SerializerMethodField()
    
    def get_status_verbose(self, obj):
        return obj.status_display


class AvatarSerializerMixin(serializers.ModelSerializer):
    '''
        Mixin for the adorable.io image
    '''
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, obj):
        return 'https://api.adorable.io/avatars/285/{}%40adorable.io'.format(obj.username)

