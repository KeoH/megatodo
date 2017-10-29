from django.db import models
from django.contrib.auth.models import User

from core.behaviours import UUIDableBehaviour, TimestampableBehaviour, StatustableBehaviour, DueDateBehaviour


class Todo(UUIDableBehaviour, TimestampableBehaviour,StatustableBehaviour, DueDateBehaviour):
    '''
        Todo Model
    '''
    author = models.ForeignKey(User, related_name='todos')
    title  = models.CharField(max_length=255)
    body   = models.TextField()

    def __str__(self):
        return self.title

class Task(UUIDableBehaviour, TimestampableBehaviour, StatustableBehaviour, DueDateBehaviour):
    '''
        Task model
    '''
    todo = models.ForeignKey(Todo, related_name='tasks')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']

class Comment(UUIDableBehaviour, TimestampableBehaviour):
    '''
        Comment model
    '''
    author = models.ForeignKey(User, related_name='comments')
    todo = models.ForeignKey(Todo, related_name='comments')
    message = models.TextField()
