from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from todos.models import Todo, Task, Comment

from .serializers.todo import TodoSerializer
from .serializers.task import TaskSerializer
from .serializers.user import UserSerializer
from .serializers.comment import CommentSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
        Serializer for Todo model
    """
    serializer_class = TodoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(author=self.request.user)
        else:
            return Todo.objects.none()

    def create(self,request):
        todo = Todo.objects.create(
            author=request.user,
            title = request.data.get('title'),
            body = request.data.get('body')
        )
        return Response(TodoSerializer(todo).data, status=201)


class TaskViewSet(viewsets.ModelViewSet):
    """
        Serializer for Task model
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    """
        Serializer for User model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
        Serializer for Todo model
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
        try:
            author = User.objects.get(username=request.data.get('author'))
        except Exception:
            return Response({"error":"Author not found"}, status=400)
        try:
            todo = Todo.objects.get(pk=request.data.get('todo'))
        except Exception:
            return Response({"error":"ToDo not found"}, status=400)
        
        comment = Comment.objects.create(
            author=author,
            message=request.data.get('message'),
            todo = todo
        )
        return Response(CommentSerializer(comment).data, status=201)
