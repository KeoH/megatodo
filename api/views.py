from django.contrib.auth.models import User
from rest_framework import viewsets

from todos.models import Todo

from .serializers.todo import TodoSerializer
from .serializers.user import UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        print(type(self.request.auth))
        if self.request.user.is_authenticated:
            return Todo.objects.filter(author=self.request.user)
        else:
            return Todo.objects.none()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer