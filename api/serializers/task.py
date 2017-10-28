from rest_framework import serializers

from todos.models import Task

from ..mixins.serializers import StatusSerializerMixin

class TaskSerializer(StatusSerializerMixin):

    class Meta:
        model = Task
        fields = ('id','title','todo','status', 'status_verbose','create_date', 'update_date')
