from django.contrib.auth.models import User
from rest_framework import viewsets

from todos.models import Todo, Task, Comment

from .serializers.todo import TodoSerializer
from .serializers.task import TaskSerializer
from .serializers.user import UserSerializer
from .serializers.comment import CommentSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(author=self.request.user)
        else:
            return Todo.objects.none()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer